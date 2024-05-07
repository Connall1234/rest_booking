from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

class Booking(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    special_occasion = models.CharField(max_length=11, choices=[('None', 'None'), ('anniversary', 'Anniversary'), ('date', 'Date'), ('business', 'Business')])
    meal_day = models.DateField()
    number_of_guests = models.PositiveIntegerField(
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    customer_name = models.CharField(max_length=50)
    is_booked = models.BooleanField(default=False)  # Indicates whether the time slot is booked or not

    def clean(self):
        # This stops the user from booking in the past 
        if self.meal_day and self.meal_day < now().date():
            raise ValidationError("Cannot make a booking in the past.")

        # This checks for bookings at the same time 
        existing_bookings = Booking.objects.filter(meal_time=self.meal_time, meal_day=self.meal_day, is_booked=True)
        if self.pk:  # Exclude current booking from choices 
            existing_bookings = existing_bookings.exclude(pk=self.pk)
        if existing_bookings.exists():
            raise ValidationError("A booking already exists at this time on this day.")

    TIME_CHOICES = [
        ('13:00', '01:00 PM'),
        ('14:00', '02:00 PM'),
        ('15:00', '03:00 PM'),
        ('16:00', '04:00 PM'),
        ('17:00', '05:00 PM'),
        ('18:00', '06:00 PM'),
        ('19:00', '07:00 PM'),
        ('20:00', '08:00 PM'),
    ]

    meal_time = models.CharField(max_length=5, choices=TIME_CHOICES)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if it's a new booking
            available_times = [choice[0] for choice in self.TIME_CHOICES]
            booked_times = Booking.objects.filter(meal_day=self.meal_day, is_booked=True).values_list('meal_time', flat=True)
            available_times = [time for time in available_times if time not in booked_times]
            if available_times:
                self.meal_time = available_times[0]  # Assign the first available time slot
                self.is_booked = True  # Mark the time slot as booked
            else:
                raise ValidationError("No available time slots for the selected day.")
        super().save(*args, **kwargs)



#def main():
    # Fetch the booking with pk 1
    #booking_pk_1 = Booking.objects.filter(pk=21).first()

    # Print the booking information
    #if booking_pk_1:
       # print("Booking with pk 21:")
       # print("Name:", booking_pk_1.name)
       # print("Special Occasion:", booking_pk_1.special_occasion)
       # print("Meal Day:", booking_pk_1.meal_day)
       # print("Number of Guests:", booking_pk_1.number_of_guests)
       # print("Customer Name:", booking_pk_1.customer_name)
       # print("Meal Time:", booking_pk_1.meal_time)
        # Add more fields as needed
    #else:
       # print("Booking with pk 21 does not exist.")


#main()

#print("Hello")