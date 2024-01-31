from django.db import models
from django.urls import reverse


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rooms', kwargs={'room_slug': self.slug})


class Comment(models.Model):
    nickname = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Room', on_delete=models.CASCADE)

