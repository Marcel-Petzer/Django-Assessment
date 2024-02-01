from django.db import models

class Drone(models.Model):
    SERIAL_NUMBER_MAX_LENGTH = 100
    MODEL_CHOICES = [
        ('lightweight', 'Lightweight'),
        ('middleweight', 'Middleweight'),
        ('cruiseweight', 'Cruiseweight'),
    ]
    serial_number = models.CharField(max_length=SERIAL_NUMBER_MAX_LENGTH)
    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    weight_limit = models.IntegerField(default=500)
    battery_capacity = models.IntegerField()
    state = models.CharField(max_length=10, choices=[
        ('idle', 'Idle'),
        ('loading', 'Loading'),
        ('loaded', 'Loaded'),
        ('delivering', 'Delivering'),
        ('delivered', 'Delivered'),
        ('returning', 'Returning'),
    ])

    def __str__(self):  
        return self.serial_number


class Medication(models.Model):
    NAME_MAX_LENGTH = 100
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    weight = models.FloatField()
    code = models.CharField(max_length=10, unique=True)
  

    def __str__(self):
        return self.name



from django.db import models

class DM_Package(models.Model):
    medicationID = models.IntegerField()
    droneID = models.IntegerField()
    loaded_item_name = models.CharField(max_length=100)
    drone_availability = models.CharField(max_length=20)
    drone_battery_life = models.IntegerField()

    def __str__(self):
        return self.loaded_item_name