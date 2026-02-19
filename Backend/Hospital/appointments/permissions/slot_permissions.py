from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsDoctorOwnerOrAdmin(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True

        return request.user.role in ["DOCTOR", "ADMIN"]


    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.role == "ADMIN"
            or obj.doctor.user == request.user
        )
