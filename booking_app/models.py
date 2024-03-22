from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, Group, Permission

class Airport(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Flight(models.Model):
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Flight from {self.departure_airport} to {self.arrival_airport}"

class User(AbstractUser, PermissionsMixin):
    user = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user',
    )

class Place(models.Model):
    place = models.CharField(max_length=3)
    num = models.IntegerField()
    clas = models.CharField(max_length=1)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)