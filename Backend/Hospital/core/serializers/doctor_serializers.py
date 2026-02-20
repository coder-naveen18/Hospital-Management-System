from rest_framework import serializers
from core.models import Doctor


class DoctorListSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(
        source="user.get_full_name",
        read_only=True
    )

    department = serializers.CharField(
        source="department.name",
        read_only=True
    )

    class Meta:
        model = Doctor
        fields = [

            "id",
            "doctor_id",
            "full_name",
            "department",
            "specialization",
            "consultation_fee",
            "is_available"

        ]


class DoctorDetailSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(
        source="user.get_full_name",
        read_only=True
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    phone = serializers.CharField(
        source="user.phone_number",
        read_only=True
    )

    department = serializers.CharField(
        source="department.name",
        read_only=True
    )

    class Meta:
        model = Doctor
        fields = [

            "id",
            "doctor_id",
            "full_name",
            "email",
            "phone",
            "department",
            "specialization",
            "license_number",
            "experience_years",
            "consultation_fee",
            "is_available"

        ]


class DoctorCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Doctor
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "department",
            "specialization",
            "license_number",
            "experience_years",
            "consultation_fee",
            "is_available"
        ]

    def create(self, validated_data):
        from core.models import User
        
        # Extract user data
        user_data = {
            'username': validated_data.pop('username'),
            'email': validated_data.pop('email'),
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'phone_number': validated_data.pop('phone_number', ''),
            'role': User.Roles.DOCTOR
        }
        password = validated_data.pop('password')
        
        # Create user
        user = User.objects.create_user(
            **user_data,
            password=password
        )
        
        # Create doctor with remaining data
        doctor = Doctor.objects.create(user=user, **validated_data)
        
        return doctor


class DoctorUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        source="user.first_name",
        required=False
    )
    last_name = serializers.CharField(
        source="user.last_name",
        required=False
    )

    class Meta:
        model = Doctor
        fields = [
            "first_name",
            "last_name",
            "department",
            "specialization",
            "license_number",
            "experience_years",
            "consultation_fee",
            "is_available"

        ]

        extra_kwargs = {
            field: {"required": False}
            for field in fields
        }

    def update(self, instance, validated_data):
        # Extract user data if present
        user_data = validated_data.pop('user', {})
        
        # Update user fields if provided
        if user_data:
            user = instance.user
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()
        
        # Update doctor fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance
