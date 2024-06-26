# Generated by Django 4.2.11 on 2024-05-12 13:20
"""Module for migration"""
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    """Migration class, changed fields"""
    dependencies = [
        ('bookings', '0007_remove_booking_is_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_guests',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(
                1, message='Number of guests must be at least 1.'), django.core.validators.MaxValueValidator(6, message='Number of guests cannot exceed 6.')]),
        ),
    ]
