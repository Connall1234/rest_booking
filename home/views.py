"""Module for our index URL."""
from django.shortcuts import render

"""To return our index URL."""
def index(request):
    return render(request, "index.html")

#pep8checked