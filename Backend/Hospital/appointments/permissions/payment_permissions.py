from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReceptionist(BasePermission):

    def has_permission(self, request, view):

        return request.user.role in ["ADMIN", "RECEPTIONIST"]


class IsPaymentOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):

        return (
            request.user.role == "ADMIN"
            or obj.appointment.patient.user == request.user
        )
