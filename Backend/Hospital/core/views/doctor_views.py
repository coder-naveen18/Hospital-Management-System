from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import Doctor
from core.serializers import (
    DoctorListSerializer,
    DoctorDetailSerializer,
    DoctorCreateSerializer,
    DoctorUpdateSerializer
)
from core.permissions.doctor_permissions import CanUpdateDoctor


class DoctorViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "patch"]

    queryset = Doctor.objects.select_related(
        "user",
        "department"
    ).all()

    permission_classes = [IsAuthenticated, CanUpdateDoctor]


    def get_serializer_class(self):

        if self.action == "list":
            return DoctorListSerializer

        if self.action == "retrieve":
            return DoctorDetailSerializer
        
        if self.action == "create":
            return DoctorCreateSerializer

        if self.action in ["update", "partial_update"]:
            return DoctorUpdateSerializer

        return DoctorDetailSerializer
