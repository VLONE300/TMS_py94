from django.urls import path

from .views import MainView, EditNewsView, ReadNewsView, PublishNewsView, RemoveNewsView, SendCheckNewsView, \
    AddNewsView, AddCommentView

urlpatterns = [
    path('', MainView.as_view(), name='main-page'),
    path('news/create/', AddNewsView.as_view(), name='create-news'),
    path('news/<int:pk>/', ReadNewsView.as_view(), name='read-news'),
    path('news/<int:pk>/publish/', PublishNewsView.as_view(), name='publish-news'),
    path('news/<int:pk>/edit/', EditNewsView.as_view(), name='edit-news'),
    path('news/<int:pk>/remove/', RemoveNewsView.as_view(), name='remove-news'),
    path('news/<int:pk>/send-check/', SendCheckNewsView.as_view(), name='send-check-news'),
    path('news/review/<int:pk>/', AddCommentView.as_view(), name='add-comment'),
]
