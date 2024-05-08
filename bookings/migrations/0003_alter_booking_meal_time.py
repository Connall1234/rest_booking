"""Migration for altering meal_time field in Booking model."""

from django.db import migrations, models

class Migration(migrations.Migration):
    """Migration for altering meal_time field in Booking model."""

    dependencies = [
        ('bookings', '0002_alter_booking_meal_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='meal_time',
            field=models.TimeField(),
        ),
    ]
#pep8 checked