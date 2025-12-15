from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} - {self.name}" # Return the country id and name as the string representation of the Country model


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country_id = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.name}" # Return the city id and name as the string representation of the City model