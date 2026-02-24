from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only the creator of the event can edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only allowed to creator
        return obj.created_by == request.user
