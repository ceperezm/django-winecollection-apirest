
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser

from .models import Wine
from .serializer import (WineReadSerializer, WineWriteSerializer)
from .permissions import IsClient, IsProvider, IsProviderWineOwner

class WineProviderViewSet(viewsets.ModelViewSet):
    """View set for providers to manage wines."""
    serializer_class = WineReadSerializer
    
    def get_queryset(self):
        """Get queryset for wines."""
        return Wine.objects.all()
    
    def get_permissions(self):
        if self.action == 'list':
            return [IsProvider()]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [IsProvider(), IsProviderWineOwner()]
        return [IsProvider()]

    def get_serializer_class(self):
        """Get serializer class based on action."""
        if self.action in ['create', 'update', 'partial_update']:
            return WineWriteSerializer
        return WineReadSerializer
    
class WineClientViewSet(viewsets.ReadOnlyModelViewSet):
    """View set for clients to view wines."""
    serializer_class = WineReadSerializer
    
    def get_queryset(self):
        """Get queryset for wines."""
        return Wine.objects.all()
    
    def get_permissions(self):
        """Get permissions based on action."""
        if self.action == 'list':
            return [IsAuthenticated(), IsClient()]
        elif self.action == 'retrieve':
            return [IsAuthenticated(), IsClient()]
        
        return [IsAuthenticated(), IsClient()]
    
class WinePublicListView(generics.ListAPIView):
    """Public view to list wines."""
    queryset = Wine.objects.all()
    serializer_class = WineReadSerializer
    permission_classes = [AllowAny]
                