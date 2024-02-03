from django.urls import path

from news import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsIndexView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('new_article/', views.NewArticleView.as_view(), name='new_article')
]
