from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import News


@admin.register(News)
class AutoAdmin(admin.ModelAdmin):
    search_fields = ('title',)
