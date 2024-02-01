from rest_framework import serializers
from .models import Drone, Medication,DM_Package

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ['id', 'serial_number', 'model', 'weight_limit', 'battery_capacity', 'state']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'weight', 'code']




class DM_PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DM_Package
        fields = ['medicationID', 'droneID', 'loaded_item_name', 'drone_availability', 'drone_battery_life']
# Serializer for creating a new medication associated with a drone
