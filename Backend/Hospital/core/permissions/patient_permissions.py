from rest_framework.permissions import BasePermission

class IsReceptionOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ["ADMIN", "RECEPTIONIST"]


class CanViewPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [
            "ADMIN",
            "DOCTOR",
            "NURSE",
            "RECEPTIONIST"
        ]
