from django.db import models
from locations.models import City

# Create your models here.

class Wine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    harvest_year = models.IntegerField() # Year the wine was harvested
    maker = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE) # Foreign key relationship to Attribute model
    city = models.ForeignKey(City, on_delete=models.CASCADE) # Foreign key relationship to City model
    
    
    def __str__(self): # String representation method
        return self.name # Return the wine name as the string representation of the Wine model
    

class Attribute(models.Model):
    id = models.AutoField(primary_key=True)
    total_sulfur_dioxide = models.SmallIntegerField()
    fixed_acidity = models.DecimalField(max_digits=4, decimal_places=2)
    volatile_acidity = models.DecimalField(max_digits=4, decimal_places=2)
    free_sulfur_dioxide = models.SmallIntegerField()
    citric_acid = models.DecimalField(max_digits=4, decimal_places=3)
    residual_sugar = models.DecimalField(max_digits=5, decimal_places=2)
    chlorides = models.DecimalField(max_digits=5, decimal_places=4)
    density = models.DecimalField(max_digits=7, decimal_places=5)
    pH = models.DecimalField(max_digits=3, decimal_places=2)
    sulphates = models.DecimalField(max_digits=4, decimal_places=2)
    alcohol = models.DecimalField(max_digits=4, decimal_places=2)