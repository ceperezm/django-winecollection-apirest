
from rest_framework import viewsets
from .serializer import CountrySerializer, CitySerializer
from .models import Country, City
# Create your views here.

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    
    
class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    
    
