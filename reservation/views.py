from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic, View
from .models import Reservation
from django.views.generic.edit import CreateView
from .forms import ReservationForm  # Create a form for the Reservation model

# Create your views here.


class Home(generic.DetailView):
    """
    Renders the Index page in the browser
    """
    def get(self, request):
        return render(request, 'index.html')


class Menu(generic.DetailView):
    """
    Renders the Menu page in the browser
    """
    def get(self, request):
        return render(request, 'menu.html')


class BookingView(CreateView):
    # model = Reservation
    form_class = ReservationForm
    template_name = 'booking.html'
    # success_message = "Booking successful!"

    def booking_view(self, request):
        return render(request, 'booking.html')

    def post(self, request):
        form = ReservationForm(data=request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.author = request.user
            reservation.save()

            return redirect('confirmation_page')  # Red. to confirmation page
        else:
            messages.error(request, "Invalid booking. Please ensure \
            your booking date is not in the past \
            and that a unique nickname is used.")
        return redirect('booking')  # Red. to the booking page with errors


class UserReservationsList(View):
    """
        Directs to the user's reservation page, where the get method
        retrieves all reservations made by the logged-in user.
    """

    def get(self, request,):
        reservations = Reservation.objects.filter(author=request.user)
        all_res = Reservation.objects.all()
        context = {
            'reservations': reservations,
            'all_res': all_res
        }
        return render(request, 'reservations_list.html', context)


class EditReservationView(View):
    """
    Allows the user to edit a reservation.
    """

    def get(self, request, reservation_id):
        reservation = get_object_or_404(
            Reservation,
            id=reservation_id,
            author=request.user
        )
        form = ReservationForm(instance=reservation)
        context = {
            'form': form,
            'reservation': reservation,
        }
        return render(request, 'edit_reservation.html', context)

    def post(self, request, reservation_id):
        reservation = get_object_or_404(
            Reservation,
            id=reservation_id,
            author=request.user
        )
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations_list')  # Red. to reservations list
        else:
            messages.error(request, "Invalid booking. \
            Please ensure your booking date is not in the past.")
        context = {
            'form': form,
            'reservation': reservation,
        }
        return render(request, 'edit_reservation.html', context)


class DeleteReservationView(View):
    """
    Allows the user to delete a reservation.
    """

    def get(self, request, reservation_id):
        reservation = get_object_or_404(
            Reservation,
            id=reservation_id,
            author=request.user
        )
        return render(
            request,
            'delete_reservation.html',
            {'reservation': reservation}
        )

    def post(self, request, reservation_id):
        reservation = get_object_or_404(
            Reservation,
            id=reservation_id,
            author=request.user
        )
        reservation.delete()
        return redirect('reservations_list')  # Red. to the reservations list


class ConfirmationView(View):
    """
    View for handling the confirmation page
    after a successful booking.
    """
    template_name = 'confirmation_page.html'

    def get(self, request):
        return render(request, 'confirmation_page.html')
