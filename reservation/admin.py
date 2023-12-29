from django.contrib import admin
from .models import Reservation


# Register your models here.
@admin.register(Reservation)
class BookingAdmin(admin.ModelAdmin):
    """
    class to filter and display info of the reservations
    """
    list_filter = ('update_on',)
    list_display = ('id', 'full_name', 'num_of_guests', 'notes')