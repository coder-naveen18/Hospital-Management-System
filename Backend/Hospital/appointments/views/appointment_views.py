from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from appointments.models import Appointment
from appointments.serializers import (
    AppointmentCreateSerializer,
    AppointmentListSerializer
)

from appointments.services.appointment_service import AppointmentService


class AppointmentViewSet(ModelViewSet):

    queryset = Appointment.objects.all()

    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):

        if self.action == "create":

            return AppointmentCreateSerializer

        return AppointmentListSerializer


    def perform_create(self, serializer):

        AppointmentService.create_appointment(

            patient=serializer.validated_data["patient"],

            doctor=serializer.validated_data["doctor"],

            slot=serializer.validated_data["slot"],

            booked_by=self.request.user,

            appointment_type=serializer.validated_data["appointment_type"],

            priority=serializer.validated_data["priority"],

            reason=serializer.validated_data["reason"],

        )
