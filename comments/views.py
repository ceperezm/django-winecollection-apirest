
from users.permissions import IsClient, IsOwner
from .permissions import CanViewComment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import WineComment, ClientCollectionCommment
from .serializer import (WineCommentReadSerializer,WineCommentWriteSerializer,
ClientCollectionReadCommmentSerializer,ClientCollectionWriteCommmentSerializer
)

# Wine comments

class WineCommentViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return WineComment.objects.none()

        if user.role == 'client':
            return WineComment.objects.select_related('wine','client')

        if user.role == 'provider':    
            return WineComment.objects.filter(wine__provider=user).select_related('wine','client')

        return WineComment.objects.none()
    
    def get_permissions(self):
        """
        Docstring for get_permissions
        
        :param self: Description
        """
        if self.action == 'list':
            return [IsAuthenticated()]
        elif self.action == 'retrieve':
            return [CanViewComment()]
        elif self.action in ['create', 'update', 'partial_update']:
            return [IsClient(),IsOwner()]
        return [IsAuthenticated()]


    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return WineCommentWriteSerializer
        return WineCommentReadSerializer
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
            
    
class ClientCollectionCommmentViewSet(viewsets.ModelViewSet):
    queryset = ClientCollectionCommment.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        """
        Docstring for get_permissions
        
        :param self: Description
        """
        if self.action in ['list','retrieve']:
            return [IsClient()]
        elif self.action in ['create', 'update', 'partial_update']:
            return [IsClient(),IsOwner()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ClientCollectionWriteCommmentSerializer
        return ClientCollectionReadCommmentSerializer


    def perform_create(self, serializer):
        serializer.save(client=self.request.user)