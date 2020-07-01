from rest_framework import permissions


class AuthorCustomPermission(permissions.BasePermission):

    anonymous_actions = ()
    authorized_actions = ("retrieve", "list")

    @staticmethod
    def _is_authenticated(request):
        return request.user and request.user.is_authenticated

    @classmethod
    def _is_admin(cls, request):
        return cls._is_authenticated(request) and request.user.is_superuser

    def has_permission(self, request, view):
        return any((self._is_admin(request), self._is_authenticated(request)))
