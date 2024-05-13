"""
Database migration for altering the meal_time..

This migration alters the meal_time field in bookings app.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Database migration for altering the meal_time..

    This migration alters the meal_time field in bookings app.
    """

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='meal_time',
            field=models.CharField(
                choices=[
                    ('12:00', '12:00'),
                    ('13:00', '13:00'),
                    ('14:00', '14:00')
                ],
                max_length=6
            ),
        ),
    ]
