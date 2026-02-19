from rest_framework import serializers
from appointments.models import Payment


class PaymentCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Payment

        fields = [

            "appointment",
            "amount"

        ]


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Payment

        fields = "__all__"
