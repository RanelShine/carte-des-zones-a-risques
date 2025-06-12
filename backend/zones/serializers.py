from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import RiskZone, RiskCategory

class RiskZoneSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RiskZone
        geo_field = "geometry"
        fields = ('id', 'name', 'description', 'category', 'commune', 'image_preview', 'created_at')

class RiskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskCategory
        fields = '__all__'