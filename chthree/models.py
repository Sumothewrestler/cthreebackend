# cthree/models.py

from django.db import models
from django.core.validators import MinValueValidator

class Business(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Businesses"
        ordering = ['name']

class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        CREDIT = 'Cr', 'Credit'
        DEBIT = 'Dr', 'Debit'

    date = models.DateField()
    business = models.ForeignKey(
        Business, 
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    transaction_type = models.CharField(
        max_length=2,
        choices=TransactionType.choices
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business.name} - {self.transaction_type} - {self.amount}"

    class Meta:
        ordering = ['-date', '-created_at']