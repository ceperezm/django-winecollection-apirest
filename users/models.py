from django.db import models
from locations.models import City

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    registration_date = models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username # Return the username as the string representation of the Client model
    
class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone_number = models.CharField(max_length=10)
    identifier_number = models.CharField(max_length=20, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE) # Foreign key relationship to City model
    registration_date = models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name # Return the provider name as the string representation of the Provider model    
    
    
    
