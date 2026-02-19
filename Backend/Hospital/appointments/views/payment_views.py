from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from appointments.models import Payment, Appointment

from appointments.serializers import PaymentCreateSerializer, PaymentSerializer

from appointments.services.payment_service import PaymentService


class PaymentViewSet(ModelViewSet):

    queryset = Payment.objects.all()

    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):

        if self.action == "create":

            return PaymentCreateSerializer

        return PaymentSerializer


    def perform_create(self, serializer):

        appointment = serializer.validated_data["appointment"]

        amount = serializer.validated_data["amount"]

        PaymentService.process_payment(

            appointment=appointment,

            amount=amount,

            transaction_id="TXN123"

        )
