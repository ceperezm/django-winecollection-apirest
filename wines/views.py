
from rest_framework import viewsets
from .serializer import WineReadSerializer,WineWriteSerializer, AttributeSerializer
from .models import Wine, Attribute
# Create your views here.

class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return WineWriteSerializer
        return WineReadSerializer
    
    
class AttributeViewSet(viewsets.ModelViewSet):
    serializer_class = AttributeSerializer
    queryset = Attribute.objects.all()    


