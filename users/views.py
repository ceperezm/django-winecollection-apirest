
from rest_framework import viewsets
from .serializer import ClientSerializer, ProviderSerializer
from .models import Client, Provider
# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    
        
