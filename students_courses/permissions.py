from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_superuser:
            return True
        return False
