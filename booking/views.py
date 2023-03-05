from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


class HomePage(TemplateView):
    template_name = "index.html"


# class MakeBooking(TemplateView):
#     template_name = "make_booking.html"


@login_required
def make_booking(request):
   
    if request.method == 'POST':
        booking = Booking(user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('make_booking')
    else:
        form = BookingForm()
    return render(request, 'make_booking.html', {'form': form}) 


@login_required
def view_booking(request):
    """
    Lets staff member view all bookings, and
    regular user only his own bookings.
    """
    if request.user.is_staff:
        bookings = Booking.objects.all()
    else:
        bookings = request.user.bookings.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'my_account.html', context)   


# @login_required
# def delete_booking(request, booking_id):
#     """
#     Deletes booking and sends an email to the user who placed it.
#     John at tutor support helped med figure out this one.
#     """
#     if request.user.is_staff:
#         try:
#             booking = get_object_or_404(PlaceBooking, id=booking_id)
          
#             booking.delete()
#             messages.success(request, 'Booking deleted successfully.')
#             return redirect('my_account')
#         except Http404 as err:
#             messages.error(request, 'Oops, booking not found.')
#             return redirect('my_account')
#     else:
#         return redirect('home')


@login_required
def delete_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    item.delete()
    return redirect('home')     


# class EditBooking(TemplateView):
#     template_name = "edit_booking.html"


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = BookingForm(instance=booking)
    context = {
             'form': form
    }
    return render(request, 'edit_booking.html', context)

