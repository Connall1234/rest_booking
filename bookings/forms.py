from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    # Define a date picker widget for the meal_day field
    meal_day = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    meal_time = forms.CharField(max_length=6, widget=forms.Select(attrs={'class': 'meal-time'}))

    class Meta:
        model = Booking
        fields = ['special_occasion', 'meal_day', 'meal_time', 'number_of_guests', 'customer_name']

    def clean(self):
        cleaned_data = super().clean()

        try:
            self.instance.clean()  # Trigger the model's clean method
        except ValidationError as e:
            self.add_error(None, e.message)  # Add the model's validation error to the form
            if 'meal_time' in e.message_dict:
                self.fields['meal_time'].widget.attrs.update({'class': 'meal-time taken'})  # Add custom class for taken time

        return cleaned_data
