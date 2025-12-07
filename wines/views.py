
from rest_framework import viewsets
from .serializer import WineSerializer, AttributteSerializer
from .models import Wine, Attribute
# Create your views here.

class WineViewSet(viewsets.ModelViewSet):
    serializer_class = WineSerializer
    queryset = Wine.objects.all()
    
    
class AttributeViewSet(viewsets.ModelViewSet):
    serializer_class = AttributteSerializer
    queryset = Attribute.objects.all()    


