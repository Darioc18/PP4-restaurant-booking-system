from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.

class Reservation(models.Model):
    TIME_SLOTS = (
        (None, '---------'),  # Blank option
        (0,'12.30am'),
        (1, '1.00pm'),
        (2, '1.30pm'),
        (3, '2.00pm'),
        (4, '2.30pm'),
        (5, '8.00pm'),
        (6, '8.30pm'),
        (7, '9.00pm'),
        (8, '9.30pm'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reservation"
    )
    num_of_guests = models.IntegerField(validators=[MinValueValidator(1)])
    created_on = models.DateTimeField(default=datetime.now,editable=False)
    update_on = models.DateTimeField(auto_now=True)
    date_of_booking = models.DateField(default=datetime.now)
    time_of_booking = models.IntegerField(choices=TIME_SLOTS,default=0)
    notes = models.TextField(blank=True,null=True)
    full_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50,unique=True,blank=True,null=True)

    class Meta:
        """Meta class for Reservation model"""
        ordering = ['created_on']
        

    def __str__(self):
        return f"Reservation by {self.full_name}"