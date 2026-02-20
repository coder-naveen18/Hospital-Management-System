from rest_framework.permissions import BasePermission

class CanUpdateDoctor(BasePermission):
    """
    Permission to allow:
    - Admins to create and update any doctor profile
    - Doctors to only update their own profile
    - Read-only access for everyone else
    """
    def has_permission(self, request, view):
        # Allow all authenticated users to view
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.is_authenticated
        
        # Only admins can create new doctors
        if request.method == 'POST':
            return request.user.is_authenticated and request.user.role == 'ADMIN'
        
        # For other write operations, must be authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read access to all authenticated users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Admin can update any doctor
        if request.user.role == 'ADMIN':
            return True
        
        # Doctor can only update their own profile
        if hasattr(request.user, 'doctor'):
            return obj.id == request.user.doctor.id
        
        # Deny all other write operations
        return False