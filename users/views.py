
from rest_framework import viewsets, generics
from .serializer import ProviderSerializer, ClientSerializer
from .models import Client, Provider
# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ClientRegisterView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
class ProviderRegisterView(generics.CreateAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()        
         
        
