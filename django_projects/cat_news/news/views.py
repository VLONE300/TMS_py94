from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .models import News, Author
from .forms import LoginForm, RegisterForm


# Create your views here.
class NewsIndexView(View):

    def get(self, request):
        sorting_param = request.GET.get('name_sorting', '')
        priority_sorting = request.GET.get('priority_sorting', '')
        news = News.objects.order_by(f'{priority_sorting}{sorting_param}' or 'pk')
        return render(request, 'news/index.html', context={"news": news})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'news/profile.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news:profile')
            else:
                form.add_error(None, 'Invalid email or password')

        return render(request, 'news/profile.html', {'form': form})


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('news.profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
