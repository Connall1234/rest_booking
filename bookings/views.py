from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

#This is our view to create a booking, added login required decorater
@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.name = request.user
            booking.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('booking_list')  # Change to to booking list page
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

#This is our view to edit a booking, added login required decorater
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.name != request.user:
        messages.error(request, 'You do not have permission to edit this booking.')
        return redirect('booking_list')  # Change to booking list page
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('booking_list')  # Change to booking list page
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit_booking.html', {'form': form})

#This is our view to delete a booking, added login required decorater
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.name != request.user:
        messages.error(request, 'You do not have permission to delete this booking.')
        return redirect('booking_list')  # Redirect to booking list page
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('booking_list')  # Redirect to booking list page
    return render(request, 'delete_booking.html', {'booking': booking})

#This is our view to see booking lists, added login required decorater
@login_required
def booking_list(request):
    if request.user.is_superuser:
        bookings = Booking.objects.all()
        print(bookings)
    else:
        bookings = Booking.objects.filter(name=request.user)
        print(bookings)

    return render(request, 'booking_list.html', {'bookings': bookings})
