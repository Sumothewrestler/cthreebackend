# cthree/serializers.py

from rest_framework import serializers
from .models import Business, Transaction

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class TransactionSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(source='business.name', read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'id', 'date', 'business', 'business_name',
            'transaction_type', 'amount', 'description',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        if data['amount'] <= 0:
            raise serializers.ValidationError(
                {"amount": "Amount must be greater than 0"}
            )
        return data