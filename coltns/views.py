from rest_framework import viewsets

from .models import (
    ProviderCollection,
    ClientCollection,
    ProviderWine,
    ClientCollectionWine,
    ProviderCollectionWine,
)

from .serializer import (
    ProviderCollectionReadSerializer,
    ProviderCollectionWriteSerializer,
    ClientCollectionReadSerializer,
    ClientCollectionWriteSerializer,
    ProviderWineSerializer,
    ClientCollectionWineSerializer,
    ProviderCollectionWineSerializer,
)

from .permissions import (
    IsProvider,
    IsClient,
    IsProviderCollectionOwner,
    IsClientCollectionOwner,
    IsProviderWineOwner,
    IsClientCollectionWineOwner,
    IsProviderCollectionWineOwner,
)

# Provider collections
class ProviderCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderCollectionReadSerializer

    def get_queryset(self):
        return ProviderCollection.objects.all()

    def get_permissions(self):
        if self.action == "list":
            return [IsProvider()]
        elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [IsProvider(), IsProviderCollectionOwner()]
        return [IsProvider()]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ProviderCollectionWriteSerializer
        return ProviderCollectionReadSerializer

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)

# Client collections
class ClientCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = ClientCollectionReadSerializer

    def get_queryset(self):
        return ClientCollection.objects.all()

    def get_permissions(self):
        if self.action == "list":
            return [IsClient()]
        elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [IsClient(), IsClientCollectionOwner()]
        return [IsClient()]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ClientCollectionWriteSerializer
        return ClientCollectionReadSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

# Provider Wines
class ProviderWineViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderWineSerializer

    def get_queryset(self):
        return ProviderWine.objects.all()

    def get_permissions(self):
        if self.action == "list":
            return [IsProvider()]
        elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [IsProvider(), IsProviderWineOwner()]
        return [IsProvider()]


# Client collection wines
class ClientCollectionWineViewSet(viewsets.ModelViewSet):
    serializer_class = ClientCollectionWineSerializer

    def get_queryset(self):
        return ClientCollectionWine.objects.all()

    def get_permissions(self):
        if self.action == "list":
            return [IsClient()]
        elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [IsClient(), IsClientCollectionWineOwner()]
        return [IsClient()]


# Provider collection wines
class ProviderCollectionWineViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderCollectionWineSerializer

    def get_queryset(self):
        return ProviderCollectionWine.objects.all()

    def get_permissions(self):
        if self.action == "list":
            return [IsProvider()]
        elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [IsProvider(), IsProviderCollectionWineOwner()]
        return [IsProvider()]
