"""
Module defining URL patterns for user authentication in a Django project.

This module defines URL patterns using the Django path function to map URLs to
views for user authentication, including login, logout, and user registration.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
]
#pep8 checked