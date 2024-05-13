"""
Migration for adding is_booked field and altering meal_time field
in Booking model.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration for adding is_booked field and altering meal_time field
    in Booking model.
    """

    dependencies = [
        ('bookings', '0003_alter_booking_meal_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='meal_time',
            field=models.CharField(
                choices=[
                    ('13:00', '01:00 PM'),
                    ('14:00', '02:00 PM'),
                    ('15:00', '03:00 PM'),
                    ('16:00', '04:00 PM'),
                    ('17:00', '05:00 PM'),
                    ('18:00', '06:00 PM'),
                    ('19:00', '07:00 PM'),
                    ('20:00', '08:00 PM')
                ],
                max_length=5
            ),
        ),
    ]
