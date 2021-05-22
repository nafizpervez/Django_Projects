from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Profiles(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields=['first_name','last_name','email','profession','location','phone']


class ProfilePic(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields=['profile_pic']
