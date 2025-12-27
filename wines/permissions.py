from rest_framework import permissions
from rest_framework.permissions import BasePermission
from coltns.models import ProviderWine

class IsClient(permissions.BasePermission):
    """
    Allows access only to users with role 'client'.
    """
    message = "User is not a client to access this resource."
    def has_permission(self, request, view):
         return (request.user.is_authenticated and request.user.role == 'client')
     
class IsProvider(permissions.BasePermission):
    """
    Allows access only to users with role 'provider'.
    """
    message = "User is not a provider to access this resource."
    def has_permission(self, request, view):
         return (request.user.is_authenticated and request.user.role == 'provider')
     
class IsProviderWineOwner(BasePermission):
    """
    Object-level permission to allow providers to manage only their own wines.
    Staff and superusers are always allowed.
    """
    message = "You do not own this wine."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True

        return (
            request.user
            and request.user.is_authenticated
            and obj.provider == request.user
        )