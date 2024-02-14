from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView

from news.models import News
from news.constants import NewsStatus

from .forms import NewsForm, CommentForm


class MainView(View):
    def get(self, request):
        all_news = News.objects.filter(is_published=True)
        return render(request, 'index.html', {'all_news': all_news})


class AddNewsView(View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'news/add_news.html', context={"form": form})

    def post(self, request):
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            return redirect('/')
        return render(request, 'news/add_news.html', {'form': form})


class EditNewsView(View):
    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        return render(request, 'news/edit_news.html', {'news': news})

    def post(self, request, pk):
        news = News.objects.get(pk=pk, user=request.user)

        news.title = request.POST["title"]
        news.content = request.POST["content"]

        image_news = request.FILES.get('image')
        if image_news:
            fs = FileSystemStorage()
            url = fs.save(image_news.name, image_news)
            news.image = url
        news.save()
        return redirect('profile')


class RemoveNewsView(View):
    def get(self, request, pk):
        News.objects.filter(pk=pk, user=request.user).delete()
        return redirect('profile')


class SendCheckNewsView(View):
    def get(self, request, pk):
        news = News.objects.get(pk=pk, user=request.user, status=NewsStatus.DRAFT)
        news.status = NewsStatus.VERIFICATION_SENT
        news.save()
        return redirect('profile')


class PublishNewsView(View):
    def get(self, request, pk):
        news = News.objects.get(pk=pk, user=request.user, status=NewsStatus.VERIFICATION_SUCCESS)
        news.is_published = True
        news.save()
        return redirect('profile')


class ReadNewsView(DetailView):
    def get(self, request, pk):
        news = News.objects.get(pk=pk, is_published=True)
        return render(request, 'news/read_news.html', {'news': news})


class AddCommentView(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        news = News.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent',None):
                form.parent_id = int(request.POST.get('parent'))
            form.name_id = request.user.id
            form.news = news
            form.save()
        return redirect(news.get_absolute_url())
