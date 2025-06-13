# zones/models.py
from django.db import models
import json

class RiskZone(models.Model):
    RISK_TYPES = [
        ('innondations', 'Inondations'),
        ('secheresse', 'Sécheresse'),
        ('glissement de terrain', 'Glissement de terrain'),
        ('cours d\'eau', 'Cours d\'eau')
    ]
    
    name = models.CharField(max_length=200, verbose_name="Nom de la zone")
    type = models.CharField(max_length=50, choices=RISK_TYPES, verbose_name="Type de risque")
    description = models.TextField(verbose_name="Description")
    
    # Stockage des coordonnées du polygone en JSON
    coordinates = models.JSONField(
        help_text="Coordonnées du polygone au format GeoJSON"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Zone à risque"
        verbose_name_plural = "Zones à risque"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
    
    @property
    def polygon_geojson(self):
        """Retourne les coordonnées au format GeoJSON Polygon"""
        return {
            "type": "Polygon",
            "coordinates": self.coordinates
        }
    
    def get_center_coordinates(self):
        """Calcule le centre approximatif du polygone"""
        if not self.coordinates or not self.coordinates[0]:
            return None
        
        coords = self.coordinates[0]  # Premier anneau du polygone
        total_lat = sum(coord[1] for coord in coords)
        total_lng = sum(coord[0] for coord in coords)
        
        return [total_lat / len(coords), total_lng / len(coords)]