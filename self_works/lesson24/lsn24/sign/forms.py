from django import forms


class UserForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()


class Registration(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()