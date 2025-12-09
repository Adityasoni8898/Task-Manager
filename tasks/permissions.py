from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Allow only owner or admins to read or write
    """

    def has_permission(self, request, view):
        # allow logged in users
        if not request.user.is_authenticated:
            return False

        # staff is allowed
        if request.user.is_staff:
            return True

        # admin group is allowed
        if request.user.groups.filter(name="admin").exists():
            return True

        # otherwise normal permission logic continues
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.groups.filter(name="admin").exists():
            return True

        # owner only
        return obj.owner == request.user