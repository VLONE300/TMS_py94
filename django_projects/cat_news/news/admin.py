from django.contrib import admin
from django.contrib.auth.models import User

from .models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
