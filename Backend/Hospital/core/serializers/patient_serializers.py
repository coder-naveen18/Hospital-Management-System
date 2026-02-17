from datetime import date
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from ..models import Patient

class PatientRegistrationSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(method_name="calculate_age")

    class Meta:
        model = Patient
        fields = [
            "id",
            "patient_id",
            "first_name", 
            "last_name", 
            "dob", 
            "gender", 
            "phone", 
            "email", 
            "address", 
            "emergency_contact", 
            "insurance_provider", 
            "policy_number", 
            "age"
        ]
        read_only_fields = ["patient_id", "created_at","updated_at"]

    def calculate_age(self, obj):
        today = date.today()
        age = today.year - obj.dob.year
        if today < obj.dob.replace(year=today.year):
            age -= 1
        return age

    def validate_dob(self, value):
        today = date.today()
        if value > today:
            raise serializers.ValidationError("Date of birth cannot be in the future")

        # Calculate precise age taking month/day into account
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))

        if age < 0 or age > 120:
            raise serializers.ValidationError("Age must be between 0 and 120")
        return value

    def validate(self, data):
        # Prevent duplicate registration
        if Patient.objects.filter(phone=data["phone"]).exists():
            raise serializers.ValidationError("Patient with this phone already exists")

        if data.get("email"):
            if Patient.objects.filter(email=data["email"]).exists():
                raise serializers.ValidationError("Patient with this email already exists")

        return data
    
class PatientUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            "first_name",
            "last_name",
            "dob",
            "gender",
            "phone",
            "email",
            "address",
            "emergency_contact",
            "insurance_provider",
            "policy_number",
        ]
        extra_kwargs = {
            field: {"required": False}
            for field in fields
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def validate_dob(self, value):
        today = date.today()
        if value > today:
            raise serializers.ValidationError("Date of birth cannot be in the future")

        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))

        if age < 0 or age > 120:
            raise serializers.ValidationError("Age must be between 0 and 120")
        return value

# serializers.py

class PatientListSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = [
            "id",
            "patient_id",
            "first_name",
            "last_name",
            "phone",
            "gender",
            "age",
            "created_at",
            "updated_at"
        ]


# serializers.py

class PatientDetailSerializer(serializers.ModelSerializer):

    registered_by = serializers.StringRelatedField(source="user", read_only=True)
    age = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = [
            "id",
            "patient_id",
            "first_name",
            "last_name",
            "dob",
            "gender",
            "age",
            "phone",
            "email",
            "address",
            "emergency_contact",
            "insurance_provider",
            "policy_number",
            "registered_by",
            "created_at",
            "updated_at",
        ]
