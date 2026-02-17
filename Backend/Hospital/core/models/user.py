from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        DOCTOR = 'DOCTOR', 'Doctor'
        NURSE = 'NURSE', 'Nurse'
        BILLING_STAFF = 'BILLING_STAFF', 'Billing Staff'
        RECEPTIONIST = 'RECEPTIONIST', 'Receptionist'

    role = models.CharField(max_length=20, choices=Roles.choices)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"