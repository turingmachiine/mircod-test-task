from django import forms
from django.contrib.auth import get_user_model


class SignUpForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = {"username", "password"}


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
