from django import forms


class UserForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'id': 'email', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Password'}, ))


class Registration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name', 'placeholder': 'Name', 'class': 'name'}, ))
    email = forms.CharField(widget=forms.TextInput(attrs={'id': 'email', 'placeholder': 'Email', 'class': 'email'}, ))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Password', 'class': 'password'}, ))
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'repeat_password', 'placeholder': 'Repeat password', 'class': 'repeat_password'}))
