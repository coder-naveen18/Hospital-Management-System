import uuid
from django.db import models


class Slot(models.Model):

    class Status(models.TextChoices):

        AVAILABLE = "AVAILABLE"
        RESERVED = "RESERVED"
        BOOKED = "BOOKED"
        BLOCKED = "BLOCKED"


    slot_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    doctor = models.ForeignKey(
        "core.Doctor",
        on_delete=models.CASCADE,
        related_name="slots"
    )

    date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE
    )

    class Meta:

        unique_together = (

            "doctor",
            "date",
            "start_time"

        )

        indexes = [

            models.Index(fields=["doctor", "date"]),
            models.Index(fields=["status"]),

        ]

    def __str__(self):

        return f"{self.doctor_id} - {self.date} - {self.start_time}"
