from django import forms
from django.core.exceptions import ValidationError
from .constants import BAD_WORDS
from .models import Comment


class ContentArticleField(forms.Field):
    widget = forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your text'})

    def to_python(self, value):
        if not value:
            return None

        return value

    def validate(self, value):
        for phrase in BAD_WORDS:
            if phrase in value:
                raise ValidationError('Незя так писать')
        return value


class CommentCreateForm(forms.ModelForm):
    content = ContentArticleField()

    class Meta:
        model = Comment
        fields = ('nickname', 'content',)

        widgets = {
            'nickname': forms.TextInput(attrs={'id': 'nickname', 'placeholder': 'Nickname'}),
            'content': forms.TextInput(attrs={'id': 'content', 'placeholder': 'Enter your text'})
        }
