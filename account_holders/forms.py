"""
Module for a custom user registration form using Django's UserCreationForm.

This module provides a custom form, RegisterUserForm, which extends Django's
built-in UserCreationForm.
"""

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    """
    Custom user registration form.

    This form extends Djangos UserCreationForm to include additional fields:
    - email: EmailField
    - first_name: CharField
    - last_name: CharField
    """

    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        """
        Meta class for RegisterUserForm.

        model: Model from django.contrib.auth.models.
        fields: Tuple of fields to include in the form.
        Has username, first_name, last_name, email, password1, and password2.
        """

        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')
