from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    # Allow only admin users
    def has_permission(self, request, view):
        return request.user and request.user.is_staff