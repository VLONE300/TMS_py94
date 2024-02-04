from django.contrib import admin
from django.urls import path, include

from .views import MainView, RoomView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('<slug:room_slug>/', RoomView.as_view(), name='rooms'),

]
