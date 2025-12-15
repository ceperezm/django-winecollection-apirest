from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from locations.models import City

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('provider', 'Provider'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    birth_date = models.DateField(null=True, blank=True)  # client
    name = models.CharField(max_length=100, blank=True)  # client
    
    identifier_number = models.CharField(
        max_length=20, unique=True, null=True, blank=True
    )  # provider
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True
    )

    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users_user'
