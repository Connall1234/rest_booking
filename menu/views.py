"""Module for our menu URL request"""
from django.shortcuts import render

def menu(request):
    """Below redirects to the menu"""
    return render(request, "menu.html")

#pep8 checked