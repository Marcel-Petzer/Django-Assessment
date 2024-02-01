from django.shortcuts import render

from rest_framework import viewsets
from .models import Drone,Medication,DM_Package
from .Serializers import DroneSerializer,MedicationSerializer,DM_PackageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



class DroneViewSet(viewsets.ModelViewSet):
    queryset=Drone.objects.all()
    serializer_class = DroneSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset=Medication.objects.all()
    serializer_class=MedicationSerializer

    
class DM_PackageViewSet(viewsets.ModelViewSet):
    queryset = DM_Package.objects.all()
    serializer_class = DM_PackageSerializer


# Define the drone data
new_drones = [
    {'serial_number': '123478', 'model': 'lightweight', 'weight_limit': 100, 'battery_capacity': 1000, 'state': 'idle'},
    {'serial_number': '67891', 'model': 'middleweight', 'weight_limit': 200, 'battery_capacity': 2000, 'state': 'idle'},
    {'serial_number': '11223', 'model': 'marcel', 'weight_limit': 300, 'battery_capacity': 3000, 'state': 'pes'}
]
#Data for loading Drones AKA test data in JSON  format
new_PackageData = [
    {
        "medicationID": 1,
        "droneID": 101,
        "loaded_item_name": "Medication A",
        "drone_availability": "idle",
        "drone_battery_life": 80
    },
    {
        "medicationID": 2,
        "droneID": 102,
        "loaded_item_name": "Medication B",
        "drone_availability": "returing",
        "drone_battery_life": 50
    },
   
]
#Function Code

def Register_Drone():

    # Create a list of serializer instances from the data
    serializer_instances = [DroneSerializer(data=drone) for drone in new_drones]

    # Filter out the valid serializers
    valid_serializers = [serializer for serializer in serializer_instances if serializer.is_valid()]

    # Create a list of drone instances from the valid serializers
    drone_instances = [serializer.save() for serializer in valid_serializers]

    # Save the new drones to the database using the serializer's create method
    Drone.objects.bulk_create(drone_instances)

    # Print the number of drones saved
    print(f"Number of drones saved: {Drone.objects.count()}")

def loadmedication():
    # Create a list of serializer instances from the data
    serializer_instances = [DM_PackageSerializer(data=PackageData) for PackageData in new_PackageData ]

    # Filter out the valid serializers
    valid_serializers = [serializer for serializer in serializer_instances if serializer.is_valid()]

    # Create a list of drone instances from the valid serializers
    Package_instances = [serializer.save() for serializer in valid_serializers]

    # Save the new drones to the database using the serializer's create method
    Drone.objects.bulk_create(Package_instances)

    # Print the number of drones saved
    print(f"Number of drones saved: {Drone.objects.count()}")
    
def CheckDroneAvailablity(self):
    drone_availability = self.request.query_params.get('drone_availability', None)
    if drone_availability is not None:
            drone_availability = drone_availability.lower() == 'idle'
            queryset = queryset.filter(drone_availability=drone_availability)
            return queryset

def DroneBattery(self):
    queryset = DM_Package.objects.all()

    drone_battery_life = self.request.query_params.get('drone_battery_life', None)
    if drone_battery_life is not None:
        try:
            drone_battery_life = int(drone_battery_life)
            queryset = queryset.filter(drone_battery_life__lt=drone_battery_life)
        except ValueError:
            pass

    return queryset

def DroneMedCheck(self, request, *args, **kwargs):
    queryset = DM_Package.objects.filter(drone_availability=True)
    grouped_queryset = queryset.order_by('droneID').values('droneID').annotate(loaded_medications=ArrayAgg('loaded_item_name'))
    serializer = DM_PackageSerializer(grouped_queryset, many=True)
    return Response(serializer.data)