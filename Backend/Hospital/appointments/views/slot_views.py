from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from appointments.models import Slot
from appointments.serializers.slot_serializers import (
    SlotCreateSerializer,
    SlotListSerializer,
    SlotDetailSerializer
)


class SlotViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]


    def get_queryset(self):

        doctor_id = self.request.query_params.get("doctor")
        date = self.request.query_params.get("date")

        if doctor_id and date:

            return Slot.objects.filter(
                doctor_id=doctor_id,
                date=date,
                status=Slot.Status.AVAILABLE
            ).order_by("start_time")

        return Slot.objects.all()


    def get_serializer_class(self):

        if self.action == "create":
            return SlotCreateSerializer

        if self.action == "retrieve":
            return SlotDetailSerializer

        return SlotListSerializer
