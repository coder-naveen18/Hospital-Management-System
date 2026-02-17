from django.db import models
from django.conf import settings

class Nurse(models.Model):
    nurse_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    department = models.CharField(max_length=100)
    shift = models.CharField(max_length=20)

    def __str__(self):
        return f"Nurse {self.user.get_full_name()} - {self.department}"
    

class BillingStaff(models.Model):
    billing_staff_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"Billing Staff {self.user.get_full_name()} - {self.department}"
    
    
class Receptionist(models.Model):
    receptionist_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"Receptionist {self.user.get_full_name()} - {self.department}"