""" Ulrs for our bookings"""
from django.urls import path
from . import views

urlpatterns = [
    path('create_booking/', views.create_booking, name="create_booking"),
    path('edit_booking/<booking_id>/', views.edit_booking, name = 'edit_booking'),
    path('delete_booking/<booking_id>/', views.delete_booking, name = 'delete_booking'),
    path('booking_list/', views.booking_list, name = 'booking_list'),
    path('reservationbooking_list/', views.filter_view, name='filter_view'),

]