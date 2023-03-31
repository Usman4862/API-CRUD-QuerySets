from rest_framework.permissions import *

class MyPermission(BasePermission):
    # def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
    #         return True
    #     return False
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'PUT', 'DELETE', 'POST', 'PATCH', 'HEADER', 'OPTIONS']:
            return True
        return obj.author == request.user
