from rest_framework import viewsets
from .models import Drone,Medication,DM_Package
from .Serializers import DroneSerializer,MedicationSerializer,DM_PackageSerializer



class DroneViewSet(viewsets.ModelViewSet):
    queryset=Drone.objects.all()
    serializer_class = DroneSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset=Medication.objects.all()
    serializer_class=MedicationSerializer

class DM_PackageViewSet(viewsets.ModelViewSet):
    queryset = DM_Package.objects.all()
    serializer_class = DM_PackageSerializer
  