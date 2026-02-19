import uuid
from django.db import models


class Payment(models.Model):

    class Status(models.TextChoices):

        PENDING = "PENDING"
        SUCCESS = "SUCCESS"
        FAILED = "FAILED"


    payment_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    appointment = models.OneToOneField(
        "appointments.Appointment",
        on_delete=models.CASCADE,
        related_name="payment"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)