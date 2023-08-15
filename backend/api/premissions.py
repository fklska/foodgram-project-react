from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorizedOrAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return request.user.is_authenticated
        return request.user == obj.author or request.method in SAFE_METHODS
