from rest_framework import serializers
from appointments.models import Slot


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
