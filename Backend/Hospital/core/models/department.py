from django.db import models
import uuid

class Department(models.Model):
    class DepartmentChoices(models.TextChoices):
        FRONTDESK = 'Frontdesk', 'Frontdesk'
        DOCTOR = 'Doctor', 'Doctor'
        NURSE = 'Nurse', 'Nurse'
        ADMINISTRATION = 'Administration', 'Administration'
        LABORATORY = 'Laboratory', 'Laboratory'


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100,choices=DepartmentChoices.choices, unique=True)

    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "departments"


    def __str__(self):
        return self.name
