from rest_framework import permissions
from rest_framework.permissions import BasePermission
from coltns.models import ProviderWine

class IsClient(permissions.BasePermission):
    """Permission to check if the user is a client."""
    message = "User is not a client to access this resource."
    def has_permission(self, request, view):
         return (request.user.is_authenticated and request.user.role == 'client')
     
class IsProvider(permissions.BasePermission):
    """Permission to check if the user is a provider."""
    message = "User is not a provider to access this resource."
    def has_permission(self, request, view):
         return (request.user.is_authenticated and request.user.role == 'provider')
     
class IsProviderWineOwner(BasePermission):
    message = "You do not own this wine."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True

        return ProviderWine.objects.filter(
            provider=request.user,
            wine=obj
        ).exists()