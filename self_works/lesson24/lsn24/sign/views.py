from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import UserLsn24
from .forms import UserForm, Registration
from .funcs import validator, hide_email


# Create your views here.
class SignUpView(View):
    users = UserLsn24.objects.all()

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        repeat_password = request.POST.get("repeat_password")
        password = request.POST.get("password")

        try:
            if password == repeat_password:
                UserLsn24.objects.create(name=name, email=email, password=password)
                messages.success(request, 'Successfully :D')
                return redirect('sign_up')
        except IntegrityError:
            messages.error(request, 'This email already exists')
            return redirect('sign_up')
        else:
            messages.error(request, 'Wrong confirmation password')
            return redirect('sign_up')

    def get(self, request):
        registration_form = Registration()
        return render(request, 'signup.html', context={'forms': registration_form, 'title': 'Sign Up'})


class SignInView(View):
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get('password')
        try:
            if validator(email, password):
                messages.success(request, f'Hello {UserLsn24.objects.get(email=email).name}')
                return redirect('sign_in')
        except ObjectDoesNotExist:
            messages.error(request, 'Wrong email or password')
        else:
            messages.error(request, 'Wrong email or password')
        return redirect('sign_in')

    def get(self, request):
        user_form = UserForm()
        return render(request, 'signin.html', {'forms': user_form, 'title': 'Sign In'})


class MainView(View):
    def get(self, request):
        users = hide_email()
        return render(request, 'main.html', context={'users': users, 'title': 'Main Page'})
