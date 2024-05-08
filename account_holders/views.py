"""
Module defining user authentication views for a Django project.

This module provides views for user authentication, including login,
logout, and registration.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


def login_user(request):
    """
    View for user login.

    Handles both GET and POST requests. On POST request, attempts to
    authenticate the user using the provided credentials. If
    authentication succeeds, logs the user in and redirects to the index
    page. If authentication fails, displays an error message and redirects
    to the index page.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Logged In!"))
            return redirect('index')
        else:
            messages.success(request, ("There was an error logging in"))
            return redirect('index')
    else:
        return render(request, 'authentication/login.html', {})


def logout_user(request):
    """
    View for user logout.

    Logs the user out and redirects to the index page.
    """
    logout(request)
    messages.success(request, ("You're logged out!"))
    return redirect('index')


def register_user(request):
    """
    View for user registration.

    Handles both GET and POST requests. On POST request, attempts to
    register a new user using the provided form data. If registration
    succeeds, logs the user in and redirects to the index page.
    """
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("You just registered!"))
            return redirect('index')
    else:
        form = RegisterUserForm()

    return render(request, 'authentication/register_user.html', {'form': form})
#pep8 checked