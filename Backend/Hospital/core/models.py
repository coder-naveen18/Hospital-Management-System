from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model extending AbstractUser
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
    

class Doctor(models.Model):
    doctor_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    experience_years = models.IntegerField()
    department = models.CharField(max_length=100)

    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"
    

class Patient(models.Model):
    patient_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)
    insurance_details = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient_id} - {self.first_name} {self.last_name}"
    
class Nurse(models.Model):
    nurse_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    department = models.CharField(max_length=100)
    shift = models.CharField(max_length=20)

    def __str__(self):
        return f"Nurse {self.user.get_full_name()} - {self.department}"

class BillingStaff(models.Model):
    billing_staff_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    department = models.CharField(max_length=100)

    def __str__(self):
        return f"Billing Staff {self.user.get_full_name()} - {self.department}"
    
class Receptionist(models.Model):
    receptionist_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    department = models.CharField(max_length=100)

    def __str__(self):
        return f"Receptionist {self.user.get_full_name()} - {self.department}"