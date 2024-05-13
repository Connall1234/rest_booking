"""Form for creating and updating bookings."""
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating and updating bookings."""

    # Define a date picker widget for the meal_day field

    class Meta:
        """Meta class for BookingForm."""
        model = Booking
        fields = [
            'special_occasion',
            'meal_day',
            'meal_time',
            'number_of_guests',
            'customer_name',
        ]

    def clean(self):
        """Clean method for BookingForm."""
        cleaned_data = super().clean()

        try:
            self.instance.clean()  # Trigger the model's clean method
        except ValidationError as e:
            # Add the model's validation error to the form
            self.add_error(None, e.message)
            if 'meal_time' in e.message_dict:
                self.fields['meal_time'].widget.attrs.update(
                    {'class': 'meal-time taken'})

        return cleaned_data
