from django.contrib.gis.db import models

class RiskCategory(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)  # ex: #ff0000

    def __str__(self):
        return self.name

class RiskZone(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(RiskCategory, on_delete=models.CASCADE)
    commune = models.CharField(max_length=100)
    geometry = models.PolygonField()
    image_preview = models.ImageField(upload_to='previews/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)