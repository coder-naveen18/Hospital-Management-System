from rest_framework_nested import routers

from appointments.views.appointment_views import AppointmentViewSet
from appointments.views.slot_views import SlotViewSet
from appointments.views.payment_views import PaymentViewSet


router = routers.DefaultRouter()

router.register("appointments", AppointmentViewSet, basename="appointments")
router.register("slots", SlotViewSet, basename="slots")
router.register("payments", PaymentViewSet, basename="payments")

urlpatterns = router.urls
