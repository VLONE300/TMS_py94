from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import News, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_published', 'get_image')
    readonly_fields = ('get_image',)
    list_filter = ('is_published',)
    search_fields = ('title',)
    actions = ['published', 'unpublished']
    form = NewsAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="60"')

    get_image.short_description = 'Image'

    def unpublished(self, request, queryset):

        row_update = queryset.update(is_published=False)
        if row_update == '1':
            massage_bit = '1 post updated'
        else:
            massage_bit = f'{row_update} posts have been updated '
        self.message_user(request, f'{massage_bit}')

    def published(self, request, queryset):

        row_update = queryset.update(is_published=True)
        if row_update == '1':
            massage_bit = '1 post updated'
        else:
            massage_bit = f'{row_update} posts have been updated '
        self.message_user(request, f'{massage_bit}')

    published.short_description = 'Published'
    published.allowed_permissions = ('change',)

    unpublished.short_description = 'Unpublished'
    unpublished.allowed_permissions = ('change',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...


admin.site.site_header = 'Cat News'
