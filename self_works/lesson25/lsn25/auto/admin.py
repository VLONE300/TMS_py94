from django.contrib import admin
from .models import Auto, BrandAuto, ModelAuto, UserAuto


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('vin_number', 'model', 'status_rent', 'brand')
    list_filter = ('status_rent', 'brand')
    search_fields = ('vin_number',)


@admin.register(BrandAuto)
class BrandAutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    ordering = ('name',)


@admin.register(ModelAuto)
class ModelAutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'count_autos')
    list_filter = ('brand',)
    ordering = ('name',)

    def count_autos(self, instance):
        count = Auto.objects.filter(model=instance).count()
        return count


@admin.register(UserAuto)
class UserAutoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone_number')
    search_fields = ('phone_number',)
