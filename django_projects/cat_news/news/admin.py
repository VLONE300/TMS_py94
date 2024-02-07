from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import News, Author


@admin.register(News)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)


admin.site.register(Author)
