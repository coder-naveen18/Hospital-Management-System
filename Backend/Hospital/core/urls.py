from rest_framework_nested import routers

from django.urls import path
from .views import SignupView, LoginView, LogoutView, PatientViewSet, DoctorViewSet, DepartmentViewSet

router = routers.SimpleRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r"departments", DepartmentViewSet, basename="departments")

# patient_router = routers.NestedDefaultRouter(router, r'patients', lookup='patient')
# patient_router.register(r'appointments', PatientAppointmentViewSet, basename='patient-appointments')



urlpatterns = [

    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view())
]

urlpatterns += router.urls