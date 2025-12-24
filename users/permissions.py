from rest_framework import permissions

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
          
class IsOwner(permissions.BasePermission):
    """Permission to check if the user is the owner of the object."""
    message = "You do not have permission to access this resource."
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        
        return obj == request.user