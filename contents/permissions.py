from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser


class IsAccountOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
            or request.user.is_superuser
        )
