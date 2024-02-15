from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    # Add an email field to the UserCreationForm
    email = forms.EmailField()

    class Meta:
        # Define the model and fields for the form
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        # Define the model and fields for the form
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # Define the model and fields for the form
        model = Profile
        fields = ['image']
