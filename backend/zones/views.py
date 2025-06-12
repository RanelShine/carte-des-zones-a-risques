from rest_framework import viewsets
from .models import RiskZone, RiskCategory
from .serializers import RiskZoneSerializer, RiskCategorySerializer

class RiskZoneViewSet(viewsets.ModelViewSet):
    queryset = RiskZone.objects.all()
    serializer_class = RiskZoneSerializer

class RiskCategoryViewSet(viewsets.ModelViewSet):
    queryset = RiskCategory.objects.all()
    serializer_class = RiskCategorySerializer