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

    class Meta:
        model = Doctor
        fields = [

            "doctor_id",
            "user",
            "department",
            "specialization",
            "license_number",
            "experience_years",
            "consultation_fee",
            "is_available"

        ]


class DoctorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = [

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
