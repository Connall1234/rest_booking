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
        validators=[MinValueValidator(1, message='Number of guests must be at least 1.'), MaxValueValidator(6, message='Number of guests cannot exceed 6.')])
    
    customer_name = models.CharField(max_length=50)

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

    def clean(self):
        if self.meal_day and self.meal_day < now().date():
            raise ValidationError("Cannot make a booking in the past.")

        existing_bookings = Booking.objects.filter(meal_time=self.meal_time, meal_day=self.meal_day)
        if self.pk:
            existing_bookings = existing_bookings.exclude(pk=self.pk)
        if existing_bookings.exists():
            raise ValidationError("A booking already exists at this time on this day.")

        super().clean()  # Call parent's clean method for remaining validations

    def save(self, *args, **kwargs):
        if not self.pk:
            available_times = [choice[0] for choice in self.TIME_CHOICES]
            booked_times = Booking.objects.filter(meal_day=self.meal_day).values_list('meal_time', flat=True)
            available_times = [time for time in available_times if time not in booked_times]
            
            print("\nAvailable times:", available_times)
            print("Booked times:", booked_times)
            print("Self pk:", self.pk)

            if available_times:
                print("\nSelf meal time before assignment:", self.meal_time)
                self.meal_time = self.meal_time
                print("Self meal time after assignment:", self.meal_time)
            else:
                raise ValidationError("No available time slots for the selected day.")
        else:
            print("\nSelf meal time before save:", self.meal_time)
        
        super().save(*args, **kwargs)

        print("Self meal time after save:", self.meal_time)
