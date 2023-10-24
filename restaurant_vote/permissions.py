from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed

class IsAuthenticatedWithJWT(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if a JWT token is present in the 'jwt' cookie
        jwt_token = request.COOKIES.get('jwt')
        if jwt_token:
            # User is authenticated; allow access
            return True
        else:
            # User is not authenticated; raise an AuthenticationFailed exception
            raise AuthenticationFailed('Unauthenticated')