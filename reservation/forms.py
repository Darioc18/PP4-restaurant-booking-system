from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    """Form to book a table"""
    class Meta:
        """Meta class"""
        model = Reservation
        fields = '__all__'
        exclude = ['author']
        widgets = {
            'date_of_booking': forms.DateInput(attrs={'type': 'datetime-local'}),
        }