from rest_framework import serializers
from appointments.models import Slot


# ✅ Serializer for creating slots
class SlotCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slot
        fields = [
            "id",
            "doctor",
            "date",
            "start_time",
            "end_time",
            "status"
        ]

        read_only_fields = ["id", "status"]


    def validate(self, attrs):

        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")
        doctor = attrs.get("doctor")
        date = attrs.get("date")

        # Validate time order
        if start_time >= end_time:
            raise serializers.ValidationError(
                "End time must be greater than start time"
            )

        # Prevent duplicate slot
        if Slot.objects.filter(
            doctor=doctor,
            date=date,
            start_time=start_time
        ).exists():
            raise serializers.ValidationError(
                "Slot already exists for this doctor at this time"
            )

        return attrs


class SlotListSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(
        source="doctor.user.get_full_name",
        read_only=True
    )

    class Meta:
        model = Slot
        fields = [
            "id",
            "slot_id",
            "doctor",
            "doctor_name",
            "date",
            "start_time",
            "end_time",
            "status"
        ]


class SlotDetailSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(
        source="doctor.user.get_full_name",
        read_only=True
    )

    department = serializers.CharField(
        source="doctor.department.name",
        read_only=True
    )

    class Meta:
        model = Slot
        fields = [
            "id",
            "slot_id",
            "doctor",
            "doctor_name",
            "department",
            "date",
            "start_time",
            "end_time",
            "status"
        ]
