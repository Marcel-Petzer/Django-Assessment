from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DroneViewSet, MedicationViewSet

router = DefaultRouter()
router.register(r'drones', DroneViewSet)
router.register(r'medications', MedicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]