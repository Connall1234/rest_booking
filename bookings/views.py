"""Module for managing bookings including creation, editing, and deletion."""
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

@login_required
def create_booking(request):
    """View function to create a booking."""
    if request.method == 'POST':
        print("Form Data:", request.POST)

        form = BookingForm(request.POST)
        if form.is_valid():
            print("\nForm Data check two:", request.POST, "\n")

            booking = form.save(commit=False)
            booking.name = request.user
            booking.save()

            messages.success(request, 'Booking created successfully!')
            return redirect('booking_list')  # Change to to booking list page
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

@login_required
def edit_booking(request, booking_id):
    """View function to edit a booking."""
    booking = get_object_or_404(Booking, pk=booking_id)
    if not request.user.is_superuser and booking.name != request.user:
        messages.error(request, 'You do not have permission to edit this booking.')
        return redirect('booking_list')  # Change to booking list page
    if request.method == 'POST':
        print("Form Data:", request.POST)
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('booking_list')  # Change to booking list page
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})

@login_required
def delete_booking(request, booking_id):
    """View function to delete a booking."""
    booking = get_object_or_404(Booking, pk=booking_id)
    if not request.user.is_superuser and booking.name != request.user:
        messages.error(request, 'You do not have permission to delete this booking.')
        return redirect('booking_list')  # Redirect to booking list page
    if request.user == request.user or request.user.is_superuser:
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('booking_list')  # Redirect to booking list page
    return render(request, 'booking_list.html', {'booking': booking})

@login_required
def booking_list(request):
    """View function to display booking lists."""
    if request.user.is_superuser:
        bookings = Booking.objects.all()
        p = Paginator(Booking.objects.all(), 10)
        page = request.GET.get('page')
        booking_list_result = p.get_page(page)

        today = date.today()
        for booking in booking_list_result:
            booking.is_past_meal_day = booking.meal_day < today
    else:
        bookings = Booking.objects.filter(name=request.user)
        p = Paginator(Booking.objects.filter(name=request.user), 2)
        page = request.GET.get('page')
        booking_list_result = p.get_page(page)
        today = date.today()
        for booking in booking_list_result:
            booking.is_past_meal_day = booking.meal_day < today

    return render(request, 'booking_list.html',
                  {'bookings': bookings, 'booking_list_result': booking_list_result})

def filter_view(request):
    """View function to filter bookings."""
    qs = Booking.objects.all()

    meal_day_query = request.GET.get('meal_day')

    if meal_day_query is not None:
        qs = qs.filter(meal_day=meal_day_query)

    today = date.today()
    for booking in qs:
        booking.is_past_meal_day = booking.meal_day < today
        print(booking.is_past_meal_day, booking.meal_day, today, "\nHelloooooo")

    context = {
        'queryset': qs
    }
    return render(request, "booking_list.html", context)
#pep8check