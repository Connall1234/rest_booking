"""Our menu URL module"""
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
]
#pep8checked