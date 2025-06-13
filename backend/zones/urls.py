# zones/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'zones', views.RiskZoneViewSet)
router.register(r'zone-images', views.RiskZoneImageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

# Dans votre urls.py principal (projet/urls.py)
from django.conf import settings
from django.conf.urls.static import static

# Ajoutez à la fin de vos urlpatterns :
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)