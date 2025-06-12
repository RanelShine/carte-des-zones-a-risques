from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiskZoneViewSet, RiskCategoryViewSet

router = DefaultRouter()
router.register(r'zones', RiskZoneViewSet)
router.register(r'categories', RiskCategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]