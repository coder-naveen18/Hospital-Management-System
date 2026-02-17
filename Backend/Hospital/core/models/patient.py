import uuid
from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
        OTHER = 'OTHER', 'Other'    

    patient_id = models.CharField(max_length=20, unique=True, editable=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=Gender.choices)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{10}$', "Phone number must be 10 digits")]
    )
    email = models.EmailField(blank=True, null=True)

    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)

    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    policy_number = models.CharField(max_length=100, blank=True, null=True)

    photo = models.ImageField(upload_to="patients/", blank=True, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="registered_patients"
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_patients"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < self.dob.replace(year=today.year):
            age -= 1
        return age

    def save(self, *args, **kwargs):
        if not self.patient_id:
            self.patient_id = "PAT-" + str(uuid.uuid4().hex[:8]).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient_id} - {self.first_name} {self.last_name}"
    
