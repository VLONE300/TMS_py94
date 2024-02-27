from django.contrib import auth
from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from slugify import slugify
from .constants import NewsStatus


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True, default='')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=NewsStatus.choices, default=NewsStatus.DRAFT)
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    url = models.SlugField(max_length=160, unique=True)

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.url})

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

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.news.url})

    def __str__(self):
        return f'{self.name} - {self.news.title}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
