from django.contrib import admin
from .models import Auto, BrandAuto, ModelAuto, UserAuto


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('vin_number', 'model', 'status_rent', 'user', 'brand')
    list_filter = ('status_rent', 'brand')
    search_fields = ('vin_number',)


@admin.register(BrandAuto)
class BrandAutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    ordering = ('name',)


@admin.register(ModelAuto)
class ModelAutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')
    list_filter = ('brand',)
    ordering = ('name',)


@admin.register(UserAuto)
class UserAutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('phone_number',)
