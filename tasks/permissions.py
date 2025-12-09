from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Allow only owner or admins to read or write
    """

    def has_object_permission(self, request, view, obj):
        # This is for read permissions
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_staff or obj.owner == request.user

        # This is for write permissions
        return request.user.is_staff or obj.owner == request.user