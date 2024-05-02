from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.db import connection


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

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if not request.user.is_superuser and booking.name != request.user:
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
    
    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})


#This is our view to delete a booking, added login required decorater
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if not request.user.is_superuser and booking.name != request.user:
        messages.error(request, 'You do not have permission to delete this booking.')
        return redirect('booking_list')  # Redirect to booking list page
    if request.user == request.user or request.user.is_superuser:
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('booking_list')  # Redirect to booking list page
    return render(request, 'booking_list.html', {'booking': booking})

#This is our view to see booking lists, added login required decorater
@login_required
def booking_list(request):
    if request.user.is_superuser:
        bookings = Booking.objects.all()
        p = Paginator(Booking.objects.all(), 2)
        page = request.GET.get('page')
        booking_list_result = p.get_page(page)
    else:
        bookings = Booking.objects.filter(name=request.user)
        p = Paginator(Booking.objects.filter(name=request.user), 2)
        page = request.GET.get('page')
        booking_list_result = p.get_page(page)

    return render(request, 'booking_list.html', {'bookings': bookings, 'booking_list_result': booking_list_result})


def filterView(request):
    qs = Booking.objects.all()
    print("\n")  # This will print a blank line
    print("This is the query", qs.query)  # Print the initial queryset SQL query
    print("\n")  # This will print a blank line


    #meal_time_query = request.GET.get('meal_time')
    #special_occasion_query = request.GET.get('special_occasion')
    meal_day_query = request.GET.get('meal_day')
    #guests_query = request.GET.get('id_number_of_guests')
    #customer_name_query = request.GET.get('customer_name')

    #print("/nThis is meal time query:", meal_time_query, "/n")
    #print("/nThis is special occ query:", special_occasion_query, "/n")
    #print("/nThis is meal day query:", meal_day_query, "/n")
    #print("/nThis is guest query:", guests_query, "/n")
    print("/nThis is meal day query:", meal_day_query, "/n")




    #if meal_time_query is not None:
        #qs = qs.filter(meal_time=meal_time_query)
    #elif special_occasion_query is not None:
       # qs = qs.filter(special_occasion=special_occasion_query)
    if meal_day_query is not None:
        qs = qs.filter(meal_day=meal_day_query)
        print("\n")  # This will print a blank line
        print("Meal day  check:", meal_day_query)
        print("\n")  # This will print a blank line
        print("\n")  # This will print a blank line
    #elif guests_query is not None:


        #guests_query_int = int(guests_query)
        ###print("\n")  # This will print a blank line
        #print("Second guest check made into int:", guests_query_int)
        #print("\n")  # This will print a blank line


        #qs = qs.filter(number_of_guests=guests_query_int)

    #elif customer_name_query is not None:



    context = {
        'queryset': qs
    }
    return render(request, "booking_list.html", context)







