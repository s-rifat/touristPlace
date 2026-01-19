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
