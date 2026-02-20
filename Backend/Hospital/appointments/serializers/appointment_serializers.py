from rest_framework import serializers
from appointments.models import Appointment, Slot


# -------------------------------
# CREATE APPOINTMENT SERIALIZER
# -------------------------------
class AppointmentCreateSerializer(serializers.ModelSerializer):

    slot = serializers.PrimaryKeyRelatedField(
        queryset=Slot.objects.none()
    )

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

    # Dynamic slot filtering based on selected doctor
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        request = self.context.get("request")

        if request and request.method in ["POST", "PUT", "PATCH"]:

            doctor_id = request.data.get("doctor")

            if doctor_id:
                self.fields["slot"].queryset = Slot.objects.filter(
                    doctor_id=doctor_id,
                    is_available=True
                )

    # Validation
    def validate(self, attrs):

        slot = attrs.get("slot")
        doctor = attrs.get("doctor")

        if slot.doctor != doctor:
            raise serializers.ValidationError(
                "Selected slot does not belong to this doctor"
            )

        if not slot.is_available:
            raise serializers.ValidationError(
                "Slot is already booked"
            )

        return attrs

    # Create appointment and lock slot
    def create(self, validated_data):

        slot = validated_data["slot"]
        request = self.context.get("request")

        appointment = Appointment.objects.create(
            booked_by=request.user,
            status=Appointment.Status.PENDING,
            **validated_data
        )

        # Lock the slot
        slot.is_available = False
        slot.save()

        return appointment


# -------------------------------
# LIST SERIALIZER
# -------------------------------
class AppointmentListSerializer(serializers.ModelSerializer):

    patient_name = serializers.SerializerMethodField()
    doctor_name = serializers.SerializerMethodField()
    slot_time = serializers.SerializerMethodField()
    slot_date = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = [
            "id",
            "appointment_id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "slot",
            "slot_date",
            "slot_time",
            "appointment_type",
            "priority",
            "reason",
            "status",
            "created_at"
        ]

    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"

    def get_doctor_name(self, obj):
        return obj.doctor.user.get_full_name()

    def get_slot_time(self, obj):
        return obj.slot.start_time

    def get_slot_date(self, obj):
        return obj.slot.date


# -------------------------------
# DETAIL SERIALIZER
# -------------------------------
class AppointmentDetailSerializer(serializers.ModelSerializer):

    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    slot = serializers.StringRelatedField()
    booked_by = serializers.StringRelatedField()

    class Meta:
        model = Appointment
        fields = "__all__"
