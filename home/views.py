"""Module for our index URL."""
from django.shortcuts import render


def index(request):
    """To return our index URL."""

    return render(request, "index.html")
