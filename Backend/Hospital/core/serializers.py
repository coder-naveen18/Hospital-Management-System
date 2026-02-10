from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User, Doctor, Nurse, BillingStaff, Receptionist

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




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        data['username'] = self.user.username
        return data
