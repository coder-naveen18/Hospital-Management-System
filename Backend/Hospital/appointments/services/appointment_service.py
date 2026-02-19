from django.db import transaction
from appointments.models import Appointment, Slot


class AppointmentService:

    @staticmethod
    @transaction.atomic
    def create_appointment(

        *,
        patient,
        doctor,
        slot,
        booked_by,
        appointment_type,
        priority,
        reason

    ):

        slot = Slot.objects.select_for_update().get(id=slot.id)

        if slot.status != Slot.Status.AVAILABLE:

            raise Exception("Slot already booked")

        slot.status = Slot.Status.BOOKED
        slot.save()

        appointment = Appointment.objects.create(

            patient=patient,
            doctor=doctor,
            slot=slot,
            booked_by=booked_by,
            appointment_type=appointment_type,
            priority=priority,
            reason=reason

        )

        return appointment
