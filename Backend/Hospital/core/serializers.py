from datetime import date
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User, Doctor, Nurse, BillingStaff, Receptionist, Patient

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','confirm_password', 'role', 'phone_number']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match"}
            )
        return data
    
    def create(self, validated_data):
        role = validated_data['role']

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role,
            phone_number=validated_data.get('phone_number')
        )

        if role == User.Roles.DOCTOR:
            Doctor.objects.create(
                user=user,
                doctor_id=f"DOC-{user.id}",
                specialization="General",
                license_number="PENDING",
                experience_years=0,
                department="General"
            )

        elif role == User.Roles.NURSE:
            Nurse.objects.create(
                user=user,
                nurse_id=f"NUR{user.id}",
                department="General",
                shift="Day"
            )

        elif role == User.Roles.BILLING_STAFF:
            BillingStaff.objects.create(
                user=user,
                billing_staff_id=f"BILL{user.id}",
                department="Accounts"
            )

        elif role == User.Roles.RECEPTIONIST:
            Receptionist.objects.create(
                user=user,
                receptionist_id=f"REC{user.id}",
                department="Front Desk"
            )

        return user



from django.utils import timezone
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        self.user.last_login = timezone.now()
        self.user.save(update_fields=['last_login'])
        data['role'] = self.user.role
        data['username'] = self.user.username
        return data


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
