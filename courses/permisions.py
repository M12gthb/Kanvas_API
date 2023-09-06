from rest_framework import permissions
from accounts.models import Account
from rest_framework.views import View


class IsLoggedOrSuperuser(permissions.BasePermission):
    def has_permission(
        self,
        request,
        view: View,
    ) -> bool:
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            if request.user.is_superuser:
                return True
            return False
        else:
            return False


class IsAccountOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            if request.user.is_superuser:
                return True
            return obj == request.user
        else:
            return False
