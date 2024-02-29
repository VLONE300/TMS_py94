from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, get_user_model, logout
from django.views import View

from news.models import News

User = get_user_model()


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('news_list')


class ProfileView(View):
    def get(self, request):
        user_news = News.objects.filter(user=request.user)
        return render(request, 'custom_user/profile.html', {'user_news': user_news})


class SignUpView(View):
    def get(self, request):
        return render(request, 'custom_user/sign-up.html')

    def post(self, request):
        username, password = request.POST['username'], request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('sign-in')


class SignInView(View):
    def get(self, request):
        return render(request, 'custom_user/sign_in.html')

    def post(self, request):
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('profile')

        return redirect('sign-in')
