from django.contrib import admin
from django.urls import path
from .views import SignupView, LoginView, LogoutView, PatientViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')

# patient_router = routers.NestedDefaultRouter(router, r'patients', lookup='patient')
# patient_router.register(r'appointments', PatientAppointmentViewSet, basename='patient-appointments')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view()),
    # path('api/patients/register/', PatientRegistrationView.as_view()),
    # path("api/patients/", PatientListView.as_view(), name="patient-list"),
    # path("api/patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
    # path("api/patients/<int:pk>/update/", PatientUpdateView.as_view(), name="patient-update"),
    # path("api/patients/<int:pk>/delete/", PatientDeleteView.as_view(), name="patient-delete"),
]

urlpatterns += router.urls