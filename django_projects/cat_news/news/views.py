from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from news.models import News, Category
from news.constants import NewsStatus

from .forms import NewsForm, CommentForm


class MainView(ListView):
    model = News
    queryset = News.objects.filter(is_published=True)
    # template_name = 'index.html'

    # def get(self, request):
    #     all_news = News.objects.filter(is_published=True)
    #     categories = Category.objects.all()
    #
    #     return render(request, 'index.html', {'all_news': all_news, 'categories': categories})


class ReadNewsView(DetailView):
    model = News
    slug_field = "url"
    # def get(self, request, slug):
    #     news = News.objects.get(url=slug, is_published=True)
    #     return render(request, 'news/news_detail.html', {'news': news})


class AddNewsView(CreateView):
    model = News
    form_class = NewsForm
    template_name = "news/add_news.html"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get(self, request):
    #     form = NewsForm()
    #     return render(request, 'news/add_news.html', context={"form": form})
    #
    # def post(self, request):
    #     form = NewsForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         news = form.save(commit=False)
    #         news.user = request.user
    #         news.save()
    #         return redirect('/')
    #     return render(request, 'news/add_news.html', {'form': form})


class EditNewsView(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = "news/edit_news.html"
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        return News.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        return self.get_queryset().get(url=self.kwargs['slug'])

    # def get(self, request, slug):
    #     news = News.objects.get(url=slug)
    #     return render(request, 'news/edit_news.html', {'news': news})
    #
    # def post(self, request, slug):
    #     news = News.objects.get(url=slug, user=request.user)
    #     news.title = request.POST["title"]
    #     news.content = request.POST["content"]
    #
    #     image_news = request.FILES.get('image')
    #     if image_news:
    #         fs = FileSystemStorage()
    #         url = fs.save(image_news.name, image_news)
    #         news.image = url
    #     news.save()
    #     return redirect('profile')


class RemoveNewsView(View):
    def get(self, request, slug):
        News.objects.filter(url=slug, user=request.user).delete()
        return redirect('profile')


class SendCheckNewsView(View):
    def get(self, request, slug):
        news = News.objects.get(url=slug, user=request.user, status=NewsStatus.DRAFT)
        news.status = NewsStatus.VERIFICATION_SENT
        news.save()
        return redirect('profile')


class PublishNewsView(View):
    def get(self, request, slug):
        news = News.objects.get(url=slug, user=request.user, status=NewsStatus.VERIFICATION_SUCCESS)
        news.is_published = True
        news.save()
        return redirect('profile')


class AddCommentView(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        news = News.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.name_id = request.user.id
            form.news = news
            form.save()
        return redirect(news.get_absolute_url())
