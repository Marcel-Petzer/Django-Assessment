from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import DM_PackageViewSet
from .models import DM_Package

class DM_PackageViewSetTestCase(TestCase):
    def setUp(self):
        DM_Package.objects.create(medicationID=1, droneID=101, loaded_item_name='Medication A', drone_availability='idle', drone_battery_life=27 )
        DM_Package.objects.create(medicationID=2, droneID=102, loaded_item_name='Medication B', drone_availability='idle',drone_battery_life=100)
        DM_Package.objects.create(medicationID=3, droneID=103, loaded_item_name='Medication C', drone_availability='idle',drone_battery_life=80)

    def test_check_drone_availability(self):
        request = RequestFactory().get('/api/dm_packages/', {'drone_availability': 'idle'})
        view = DM_PackageViewSet()
        view.request = request
        
        queryset = view.get_queryset()
        self.assertEqual(queryset.count(), 3)
        self.assertEqual(queryset[0].medicationID, 1)
        self.assertEqual(queryset[1].medicationID, 2)
        self.assertEqual(queryset[2].medicationID, 3)

    def test_check_drone_availability_no_parameter(self):
        request = RequestFactory().get('/api/dm_packages/')   
        view = DM_PackageViewSet()
        view.request = request
        
        queryset = view.get_queryset()
        self.assertEqual(queryset.count(), 3)



