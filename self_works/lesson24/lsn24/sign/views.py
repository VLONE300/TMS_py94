from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from sign.models import UserLsn24
from .forms import UserForm, Registration


# Create your views here.
class SignUpView(View):
    users = UserLsn24.objects.all()

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            confirm_password = request.POST.get("confirm_password")
            password = request.POST.get("password")
            if password == confirm_password:
                UserLsn24.objects.create(name=name, email=email, password=password)
                return HttpResponse(f'{email}, {password}')
            else:
                return HttpResponse('wrong confirmation email')

    def get(self, request):
        registration_form = Registration()
        return render(request, 'signup.html', context={'forms': registration_form})


class SignInView(View):
    def get(self, request):
        userform = UserForm()
        return render(request, 'signin.html', {'forms': userform})


class MainView(View):
    def get(self, request):
        users = UserLsn24.objects.all()
        return render(request, 'main.html', context={'users': users})


def validator(email):
    users_email = UserLsn24.objects.all()
    if email not in users_email.email:
        return True
