from rest_framework import serializers
from core.models.department import Department

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department

        fields = [
            "id",
            "name",
            "description",
            "is_active",
            "created_at",
            "updated_at"
        ]

        read_only_fields = ["id", "created_at", "updated_at"]
