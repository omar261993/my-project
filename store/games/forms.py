from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=254,required=True)
    password=forms.CharField(max_length=254,widget=forms.PasswordInput,required=True)
    