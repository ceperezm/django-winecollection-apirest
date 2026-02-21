from rest_framework import permissions

class CanViewComment(permissions.BasePermission):
    """Permission to check if the user can view a comment."""
    message = "User is not allowed to view this comment."
    def has_object_permission(self, request, view, obj):
        user = request.user

        # Client can view
        if user.role == 'client':
            return True

        # Provider can view
        if user.role == 'provider':
            return True

        return False    

