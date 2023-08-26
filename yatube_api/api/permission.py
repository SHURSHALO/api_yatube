from rest_framework import permissions


class OnlyAuthorHasPerm(permissions.BasePermission):
    ''' Кастомное разрешение, разрешает доступ только автору объекта. '''
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
