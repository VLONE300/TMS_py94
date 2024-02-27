from django.urls import path

from .views import MainView, EditNewsView, ReadNewsView, PublishNewsView, RemoveNewsView, SendCheckNewsView, \
    AddNewsView, AddCommentView

urlpatterns = [
    path('', MainView.as_view(), name='news_list'),
    path('news/create/', AddNewsView.as_view(), name='create-news'),
    path('news/<slug:slug>/', ReadNewsView.as_view(), name='news_detail'),
    path('news/<slug:slug>/publish/', PublishNewsView.as_view(), name='publish-news'),
    path('news/<slug:slug>/edit/', EditNewsView.as_view(), name='edit-news'),
    path('news/<slug:slug>/remove/', RemoveNewsView.as_view(), name='remove-news'),
    path('news/<slug:slug>/send-check/', SendCheckNewsView.as_view(), name='send-check-news'),
    path('news/review/<int:pk>/', AddCommentView.as_view(), name='add-comment'),
]
