from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from appointments.models import Slot
from appointments.serializers import SlotListSerializer
from appointments.services.slot_service import SlotService


class SlotViewSet(ReadOnlyModelViewSet):

    serializer_class = SlotListSerializer

    permission_classes = [IsAuthenticated]


    def get_queryset(self):

        doctor_id = self.request.query_params.get("doctor")

        date = self.request.query_params.get("date")

        if doctor_id and date:

            return SlotService.get_available_slots(

                doctor_id=doctor_id,
                date=date

            )

        return Slot.objects.none()
