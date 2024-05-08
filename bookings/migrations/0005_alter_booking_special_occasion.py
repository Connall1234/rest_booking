"""
Migration for altering special_occasion field in Booking model.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration for altering special_occasion field in Booking model.
    """

    dependencies = [
        ('bookings', '0004_booking_is_booked_alter_booking_meal_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='special_occasion',
            field=models.CharField(
                choices=[
                    (None, 'none'),
                    ('anniversary', 'Anniversary'),
                    ('date', 'Date'),
                    ('business', 'Business')
                ],
                max_length=11
            ),
        ),
    ]
#pep8 checked