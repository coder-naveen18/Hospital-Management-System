from rest_framework import serializers
from appointments.models import Appointment


class AppointmentCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Appointment

        fields = [

            "patient",
            "doctor",
            "slot",
            "appointment_type",
            "priority",
            "reason"

        ]


class AppointmentListSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(
        source="patient.first_name",
        read_only=True
    )

    doctor_name = serializers.CharField(
        source="doctor.user.get_full_name",
        read_only=True
    )

    class Meta:

        model = Appointment

        fields = "__all__"
