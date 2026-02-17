from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import Doctor
from core.serializers import (
    DoctorListSerializer,
    DoctorDetailSerializer,
    DoctorCreateSerializer,
    DoctorUpdateSerializer
)


class DoctorViewSet(ModelViewSet):

    queryset = Doctor.objects.select_related(
        "user",
        "department"
    ).all()

    permission_classes = [IsAuthenticated]


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
