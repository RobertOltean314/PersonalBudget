# Here we'll define the model for our User

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    # An additional field 'email' is added to the form
    email = forms.EmailField()

    class Meta:
        # The model associated with this form is the User model
        model = User
        # The fields in the form are 'username', 'email', 'password1', and 'password2'
        fields = ['username', 'email', 'password1', 'password2']
