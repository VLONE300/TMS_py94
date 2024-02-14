from django.contrib import auth
from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

from .constants import NewsStatus


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True, default='')

    status = models.IntegerField(choices=NewsStatus.choices, default=NewsStatus.DRAFT)
    is_published = models.BooleanField(default=False)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("read-news", kwargs={"pk": self.pk})

    def get_comment(self):
        return self.comment_set.filter(parent__isnull=True)
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Comment(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField('Comment', max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Parent')
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.news.title}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
