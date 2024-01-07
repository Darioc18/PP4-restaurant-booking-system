from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('booking/', views.BookingView.as_view(), name='booking'),  # Add the booking URL pattern
    path('reservations_list/', views.UserReservationsList.as_view(), name='reservations_list'),
    path('edit_reservation/<int:reservation_id>', views.EditReservationView.as_view(), name='edit_reservation'),
]