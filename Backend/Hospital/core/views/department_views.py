from rest_framework.viewsets import ModelViewSet
from core.models.department import Department
from core.serializers.department_serializer import DepartmentSerializer

class DepartmentViewSet(ModelViewSet):

    queryset = Department.objects.all()

    serializer_class = DepartmentSerializer
