# cthree/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from .models import Business, Transaction
from .serializers import BusinessSerializer, TransactionSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    @action(detail=True)
    def summary(self, request, pk=None):
        business = self.get_object()
        transactions = business.transactions.all()
        
        credit_sum = transactions.filter(
            transaction_type='Cr'
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        debit_sum = transactions.filter(
            transaction_type='Dr'
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            'business_name': business.name,
            'total_credit': credit_sum,
            'total_debit': debit_sum,
            'balance': credit_sum - debit_sum
        })

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = ['business', 'transaction_type', 'date']
    search_fields = ['description']
    ordering_fields = ['date', 'amount', 'created_at']