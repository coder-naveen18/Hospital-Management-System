from datetime import date
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from core.models import Doctor, Nurse, BillingStaff, Receptionist, Department

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'confirm_password',
            'role',
            'phone_number'
        ]

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({
                "confirm_password": "Passwords do not match"
            })
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        role = validated_data.get('role')

        # Create user
        user = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            role=role,
            phone_number=validated_data.get('phone_number')
        )

        """
        IMPORTANT:
        Department must be instance, not string
        Use get_or_create for default departments
        """

        if role == User.Roles.DOCTOR:

            department, _ = Department.objects.get_or_create(
                name="General"
            )

            Doctor.objects.create(
                user=user,
                doctor_id=f"DOC-{user.id}",
                specialization="General",
                license_number="PENDING",
                experience_years=0,
                consultation_fee=0, 
                department=department
            )

        elif role == User.Roles.NURSE:

            department, _ = Department.objects.get_or_create(
                name="General"
            )

            Nurse.objects.create(
                user=user,
                nurse_id=f"NUR-{user.id}",
                department=department,
                shift="Day"
            )

        elif role == User.Roles.BILLING_STAFF:

            department, _ = Department.objects.get_or_create(
                name="Accounts"
            )

            BillingStaff.objects.create(
                user=user,
                billing_staff_id=f"BILL-{user.id}",
                department=department
            )

        elif role == User.Roles.RECEPTIONIST:

            department, _ = Department.objects.get_or_create(
                name="Front Desk"
            )

            Receptionist.objects.create(
                user=user,
                receptionist_id=f"REC-{user.id}",
                department=department
            )

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        # update last login
        self.user.last_login = timezone.now()
        self.user.save(update_fields=['last_login'])

        data['role'] = self.user.role
        data['username'] = self.user.username

        return data
