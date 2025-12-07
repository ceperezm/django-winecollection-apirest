
from rest_framework import viewsets
from .serializer import ClientCollectionSerializer,ClientCollectionWineSerializer,ProviderCollectionSerializer,ProviderCollectionWineSerializer,ProviderWineSerializer
from .models import ProviderWine,ClientCollection,ClientCollectionWine,ProviderCollection,ProviderCollectionWine
# Create your views here.

class ProviderCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderCollectionSerializer
    queryset = ProviderCollection.objects.all()
    
class ProviderWineViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderWineSerializer
    queryset = ProviderWine.objects.all()
 
class ClientCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = ClientCollectionSerializer
    queryset = ClientCollection.objects.all()
    
class ClientCollectionWineViewSet(viewsets.ModelViewSet):
    serializer_class = ClientCollectionWineSerializer
    queryset = ClientCollectionWine.objects.all()
 
class ProviderCollectionWineViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderCollectionWineSerializer
    queryset = ProviderCollectionWine.objects.all()
    
                
