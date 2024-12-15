# cthree/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusinessViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'businesses', BusinessViewSet)
router.register(r'transactions', TransactionViewSet)

app_name = 'chthree'

urlpatterns = [
    path('', include(router.urls)),
]