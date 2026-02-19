from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsDoctorOrReceptionist(BasePermission):
    """
    Doctor and Receptionist can create appointments
    """

    def has_permission(self, request, view):
        return request.user.role in ["DOCTOR", "RECEPTIONIST", "ADMIN"]


class IsAppointmentOwnerOrStaff(BasePermission):
    """
    Only doctor assigned, receptionist, or admin can modify
    """

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.role == "ADMIN"
            or request.user.role == "RECEPTIONIST"
            or obj.doctor.user == request.user
        )
