from django.db import models
from django.conf import settings
from .department import Department


class Doctor(models.Model):
    doctor_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="doctors"
    )

    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    experience_years = models.IntegerField()

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"