# zones/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import RiskZone
from .serializers import RiskZoneSerializer

class RiskZoneViewSet(viewsets.ModelViewSet):
    queryset = RiskZone.objects.all()
    serializer_class = RiskZoneSerializer
    
    def get_queryset(self):
        """Filtrage optionnel par type de risque"""
        queryset = RiskZone.objects.all()
        risk_type = self.request.query_params.get('type', None)
        
        if risk_type:
            queryset = queryset.filter(type=risk_type)
        
        return queryset
    
    def create(self, request, *args, **kwargs):
        """Créer une nouvelle zone à risque"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Récupérer les zones groupées par type"""
        zones_by_type = {}
        
        for risk_type_code, risk_type_name in RiskZone.RISK_TYPES:
            zones = RiskZone.objects.filter(type=risk_type_code)
            zones_by_type[risk_type_code] = {
                'name': risk_type_name,
                'count': zones.count(),
                'zones': RiskZoneSerializer(zones, many=True).data
            }
        
        return Response(zones_by_type)
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Statistiques des zones à risque"""
        total_zones = RiskZone.objects.count()
        stats_by_type = {}
        
        for risk_type_code, risk_type_name in RiskZone.RISK_TYPES:
            count = RiskZone.objects.filter(type=risk_type_code).count()
            stats_by_type[risk_type_code] = {
                'name': risk_type_name,
                'count': count,
                'percentage': (count / total_zones * 100) if total_zones > 0 else 0
            }
        
        return Response({
            'total_zones': total_zones,
            'by_type': stats_by_type
        })