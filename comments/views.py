from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

from .models import WineComment, ClientCollectionCommment
from .serializer import (WineCommentReadSerializer,WineCommentWriteSerializer,
ClientCollectionReadCommmentSerializer,ClientCollectionWriteCommmentSerializer
)

# Wine comments

class WineCommentViewSet(viewsets.ModelViewSet):
    queryset = WineComment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return WineCommentWriteSerializer
        return WineCommentReadSerializer
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
            
    
class ClientCollectionCommmentViewSet(viewsets.ModelViewSet):
    queryset = ClientCollectionCommment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ClientCollectionWriteCommmentSerializer
        return ClientCollectionReadCommmentSerializer


    def perform_create(self, serializer):
        serializer.save(client=self.request.user)