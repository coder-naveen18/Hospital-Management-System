from appointments.models import Slot


class SlotService:

    @staticmethod
    def get_available_slots(doctor_id, date):

        return Slot.objects.filter(

            doctor_id=doctor_id,
            date=date,
            status=Slot.Status.AVAILABLE

        )
