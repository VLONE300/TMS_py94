from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import CommentCreateForm
from .models import Room, Comment


# Create your views here.
class MainView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'main.html', context={'rooms': rooms})


class RoomView(View):
    def post(self, request, room_slug):
        room = get_object_or_404(Room, slug=room_slug)
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.category = room
            comment.save()

        return render(request, 'room.html', context={'form': form})

    def get(self, request, room_slug):
        room = get_object_or_404(Room, slug=room_slug)
        comments = Comment.objects.all()
        form = CommentCreateForm()
        return render(request, 'room.html', context={'form': form, 'comments': comments, 'room': room})
