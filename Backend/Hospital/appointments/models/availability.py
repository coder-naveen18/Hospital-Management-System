from django.db import models


class Availability(models.Model):

    doctor = models.ForeignKey(
        "core.Doctor",
        on_delete=models.CASCADE,
        related_name="availabilities"
    )

    weekday = models.IntegerField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    slot_duration = models.IntegerField()

    is_active = models.BooleanField(default=True)

    class Meta:

        unique_together = (

            "doctor",
            "weekday"

        )
