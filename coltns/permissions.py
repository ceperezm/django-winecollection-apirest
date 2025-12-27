from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    message = "User is not a client."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "client"

class IsProvider(BasePermission):
    message = "User is not a provider."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "provider"

class IsProviderCollectionOwner(BasePermission):
    message = "You do not own this provider collection."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return obj.provider == request.user

class IsClientCollectionOwner(BasePermission):
    message = "You do not own this client collection."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return obj.client == request.user


class IsClientCollectionWineOwner(BasePermission):
    message = "You do not own this collection wine."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return obj.client_collection.client == request.user

class IsProviderCollectionWineOwner(BasePermission):
    message = "You do not own this provider collection wine."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return obj.provider_collection.provider == request.user
