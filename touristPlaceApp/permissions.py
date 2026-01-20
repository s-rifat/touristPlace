from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only the user who created the place can update or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Anyone can read
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only creator can write
        return obj.created_by == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Only admin users can create, update, or delete.
    Others can only read.
    """

    def has_permission(self, request, view):
        # Safe methods are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only admin users can write
        return request.user.is_staff 
