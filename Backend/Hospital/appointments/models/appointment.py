import uuid
from django.db import models


class Appointment(models.Model):

    class Status(models.TextChoices):

        PENDING = "PENDING"
        CONFIRMED = "CONFIRMED"
        CANCELLED = "CANCELLED"
        FAILED = "FAILED"


    appointment_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    patient = models.ForeignKey(
        "core.Patient",
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    doctor = models.ForeignKey(
        "core.Doctor",
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    slot = models.OneToOneField(
        "appointments.Slot",
        on_delete=models.PROTECT
    )

    booked_by = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        null=True
    )

    appointment_type = models.CharField(
        max_length=50
    )

    priority = models.CharField(
        max_length=20
    )

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
