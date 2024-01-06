from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
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
    success_message = "Booking successful!"

    def booking_view(self, request):
        return render(request, 'booking.html')

    def post(self, request):
        form = ReservationForm(data=request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.author = request.user
            reservation.save()
            return HttpResponse("Thank you for your booking. Your reservation is successful.")
        else:
            return HttpResponse("Booking incomplete. Please verify your booking details.")