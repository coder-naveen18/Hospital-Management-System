import uuid
from django.db import models


class Appointment(models.Model):

    class Status(models.TextChoices):

        PENDING = "PENDING"
        CONFIRMED = "CONFIRMED"
        CANCELLED = "CANCELLED"
        FAILED = "FAILED"

    class appointment_type(models.TextChoices):

        CONSULTATION = "CONSULTATION"
        FOLLOW_UP = "FOLLOW_UP"
        EMERGENCY = "EMERGENCY"
        ROUTINE_CHECKUP = "ROUTINE_CHECKUP"


    class priority(models.TextChoices):

        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

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
        on_delete=models.PROTECT,
        related_name="appointment"
    )

    booked_by = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        null=True
    )

    appointment_type = models.CharField(
        max_length=50,
        choices=appointment_type.choices
    )

    priority = models.CharField(
        max_length=20,
        choices=priority.choices
    )

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
