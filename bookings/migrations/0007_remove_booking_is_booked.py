"""Migration for removing is_booked field from Booking model."""
from django.db import migrations


class Migration(migrations.Migration):
    """Migration for removing is_booked field from Booking model."""
    dependencies = [('bookings', '0006_alter_booking_special_occasion'),]
    operations = [migrations.RemoveField(
        model_name='booking', name='is_booked'),]
