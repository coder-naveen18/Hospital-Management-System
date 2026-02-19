from django.db import transaction
from appointments.models import Payment, Appointment


class PaymentService:

    @staticmethod
    @transaction.atomic
    def process_payment(

        *,
        appointment,
        amount,
        transaction_id

    ):

        payment = Payment.objects.create(

            appointment=appointment,
            amount=amount,
            transaction_id=transaction_id,
            status=Payment.Status.SUCCESS

        )

        appointment.status = Appointment.Status.CONFIRMED
        appointment.save()

        return payment
