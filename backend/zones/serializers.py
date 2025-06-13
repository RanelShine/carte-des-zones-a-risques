# zones/serializers.py
from rest_framework import serializers
from .models import RiskZone

class RiskZoneSerializer(serializers.ModelSerializer):
    polygon = serializers.SerializerMethodField()
    center = serializers.SerializerMethodField()
    
    class Meta:
        model = RiskZone
        fields = [
            'id', 'name', 'type', 'description', 'coordinates', 
            'polygon', 'center', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_polygon(self, obj):
        """Retourne le polygone au format GeoJSON"""
        return obj.polygon_geojson
    
    def get_center(self, obj):
        """Retourne les coordonnées du centre"""
        return obj.get_center_coordinates()
    
    def validate_coordinates(self, value):
        """Valide le format des coordonnées"""
        if not isinstance(value, list) or not value:
            raise serializers.ValidationError("Les coordonnées doivent être une liste non vide")
        
        if not isinstance(value[0], list):
            raise serializers.ValidationError("Format de coordonnées invalide")
        
        # Vérifier que chaque point a au moins 2 coordonnées
        for point in value[0]:
            if not isinstance(point, list) or len(point) < 2:
                raise serializers.ValidationError("Chaque point doit avoir au moins 2 coordonnées")
        
        return value