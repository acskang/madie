from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class 가입폼(UserCreationForm):
    이메일 = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', '이메일', 'password1', 'password2')