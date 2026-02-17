from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..permissions.patient_permissions import IsReceptionOrAdmin, CanViewPatient
from ..models.patient import Patient
from ..serializers import (
    PatientRegistrationSerializer,
    PatientUpdateSerializer,
    PatientListSerializer, 
    PatientDetailSerializer
)
class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientRegistrationSerializer
    permission_classes = [IsAuthenticated, IsReceptionOrAdmin]
    
    def get_serializer_class(self):
        if getattr(self, 'action', None) == 'create':
            return PatientRegistrationSerializer
        if getattr(self, 'action', None) in ['update', 'partial_update']:
            return PatientUpdateSerializer
        if getattr(self, 'action', None) == 'list':
            return PatientListSerializer
        if getattr(self, 'action', None) == 'retrieve':
            return PatientDetailSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        # Use broader view permissions for listing/retrieving patients
        if getattr(self, 'action', None) in ['list', 'retrieve']:
            return [permission() for permission in [IsAuthenticated, CanViewPatient]]
        # For create/update/delete, restrict to reception/admin as before
        return [permission() for permission in [IsAuthenticated, IsReceptionOrAdmin]]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)