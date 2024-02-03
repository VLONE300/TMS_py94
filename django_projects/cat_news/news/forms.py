from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Author, News


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Author
        fields = UserCreationForm.Meta.fields + ('email',)


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content',)

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter your text'})
        }
