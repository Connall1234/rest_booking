"""
This is our module for our bookings app
"""
from django.apps import AppConfig


class BookingsConfig(AppConfig):
    """
    Class for bookings configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'
