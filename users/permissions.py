from rest_framework.permissions import BasePermission

class IsAdminUserOrAdminGroup(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_staff
            or request.user.groups.filter(name="admin").exists()
        )