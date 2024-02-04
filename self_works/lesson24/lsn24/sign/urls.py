from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.MainView.as_view(), name='mainpage'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
]
