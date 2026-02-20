from appointments.models import Slot


class SlotService:

    @staticmethod
    def create_slot(data):

        return Slot.objects.create(**data)


    @staticmethod
    def create_bulk_slots(doctor, date, start_time, end_time, duration_minutes):

        from datetime import datetime, timedelta

        slots = []

        current = datetime.combine(date, start_time)
        end = datetime.combine(date, end_time)

        while current < end:

            slot_end = current + timedelta(minutes=duration_minutes)

            slot = Slot.objects.create(
                doctor=doctor,
                date=date,
                start_time=current.time(),
                end_time=slot_end.time(),
                status=Slot.Status.AVAILABLE
            )

            slots.append(slot)

            current = slot_end

        return slots
