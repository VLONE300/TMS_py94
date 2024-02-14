from django import forms
from django.core.files.base import ContentFile

from .models import News, Comment


class NewsForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.image:
            default_image_path = 'django_projects/cat_news/news/static/news/images/0c36de30793df1f6bbb36f3e8508b67b.jpg'
            with open(default_image_path, 'rb') as f:
                default_image_data = f.read()
            instance.image.save('default_image.jpg', ContentFile(default_image_data), save=False)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = News
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter your text'}),
            'image': forms.FileInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)