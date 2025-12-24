from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import CountrySerializer, CitySerializer
from .models import Country, City
# Create your views here.

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only view for countries - public access."""
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = [IsAuthenticated]  
    
class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only view for cities - public access."""
    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = [IsAuthenticated] 
