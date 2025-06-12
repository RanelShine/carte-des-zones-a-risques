# zones/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiskZoneViewSet

router = DefaultRouter()
router.register(r'zones', RiskZoneViewSet, basename='riskzone')

urlpatterns = [
    path('api/', include(router.urls)),
]