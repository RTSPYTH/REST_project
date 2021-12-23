from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and (obj.created_by == request.user or request.user.is_staff)
        )
