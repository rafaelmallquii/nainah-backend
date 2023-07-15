from rest_framework import permissions

class IsCreatorOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # verify that the user is the creator of the object
        return obj.customer == request.user