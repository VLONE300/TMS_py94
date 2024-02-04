from django import forms
from django.core.exceptions import ValidationError
from .constants import BAD_WORDS
from .models import Comment


class ContentCommentField(forms.CharField):
    widget = forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your text'})

    def to_python(self, value):
        if not value:
            return None
        return value

    def validate(self, value):
        for phrase in BAD_WORDS:
            if phrase in value:
                raise ValidationError('Нельзя так писать')
        return value


class NicknameCommentField(forms.CharField):
    widget = forms.Textarea(attrs={'rows': 1, 'placeholder': 'Nickname'})

    def to_python(self, value):
        if not value:
            return None
        return value

    def validate(self, value):
        for phrase in BAD_WORDS:
            if phrase in value:
                raise ValidationError('Нельзя так писать')
        return value


class CommentCreateForm(forms.ModelForm):
    content = ContentCommentField()
    nickname = NicknameCommentField()

    class Meta:
        model = Comment
        fields = ('nickname', 'content',)
