from rest_framework import permissions

class IsOwnerOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.rank == 'owner' or user.rank == 'manager')