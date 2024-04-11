from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    # Define a date picker widget for the meal_day field
    meal_day = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Booking
        fields = ['special_occasion', 'meal_day', 'meal_time', 'number_of_guests', 'customer_name']
