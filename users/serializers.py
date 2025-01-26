from rest_framework import serializers

from .models import Payment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone", "city", "avatar"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "user",
            "payment_date",
            "course",
            "lesson",
            "amount",
            "payment_method",
        ]


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "payment_date", "course", "lesson", "amount", "payment_method"]


class UserProfileSerializer(serializers.ModelSerializer):
    payment_history = PaymentHistorySerializer(
        many=True, read_only=True, source="payments"
    )

    class Meta:
        model = User
        fields = ["id", "email", "phone", "city", "avatar", "payment_history"]
