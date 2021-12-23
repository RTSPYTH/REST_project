from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and (obj.added_by == request.user)
        )