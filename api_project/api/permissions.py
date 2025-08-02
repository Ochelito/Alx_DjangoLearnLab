from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        # Allow safe methods like GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True     # Allow read access for all users
       
        # Write permissions only for the author. only allow if the requesting user is the author of the object
        return obj.author == request.user