# cthree/admin.py

from django.contrib import admin
from .models import Business, Transaction

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'business', 'transaction_type',
        'amount', 'created_at'
    )
    list_filter = ('business', 'transaction_type', 'date')
    search_fields = ('description', 'business__name')
    ordering = ('-date', '-created_at')
    date_hierarchy = 'date'