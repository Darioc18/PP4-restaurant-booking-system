from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservation")
    num_of_guests = models.IntegerField()
    update_on = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    excerpt_notes = models.TextField(blank=True)
    full_name = models.CharField(max_length=20)

class Meta:
    ordering = ['created_on']

def __str__(self):
        return f"Reservation by {self.full_name}"