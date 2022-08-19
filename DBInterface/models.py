from platform import machine
from statistics import mode
import uuid
from django.db import models


# Create your models here.

class UUID(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4, null=False, editable=False)

"""
Account App's table
"""
##Account's DB table model
class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=30, default='')
    firstName = models.CharField(max_length=20, default="FirstName")
    lastName = models.CharField(max_length=20, default="LastName")
    permission = models.IntegerField(default=0)
    userStatus = models.BooleanField(default=True)

    def __str__(self):
        return self.username



"""
Device App's table

"""
##Field's DB table model
class Field(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20)
    buildingName = models.CharField(max_length=20, default='')
    floor = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name

##Machine's DB table model
class Machine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20, default='')
    model = models.CharField(max_length=20, default='')
    power = models.IntegerField(default=0)
    voltage = models.FloatField(default=0)
    electric = models.FloatField(default=0)
    photo = models.TextField(default='')
    fieldId = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

##Equlpment's DB table model
class Equlpment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20, default='')
    model = models.CharField(max_length=20, default='')
    power = models.IntegerField(default=0)
    material = models.CharField(max_length=20, default='')
    frequencyType = models.CharField(max_length=20, default='')
    rotationalSpeed = models.IntegerField(default=0)
    fladeCount = models.IntegerField(default=0)
    photo = models.TextField(default='')
    machineId = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

##Physical_Sensor_manager model
class Physical_Sensor_manager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    serialNumber = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20, default='')
    brand = models.CharField(max_length=20, default='')
    battery = models.IntegerField(default=0)
    wifi = models.IntegerField(default=0)
    cycle = models.CharField(max_length=20, default='')
    frequency = models.IntegerField(default=0)
    onlineTime = models.CharField(max_length=20, default='')
    lastUploadDataTime = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name

##Equlpment's DB table model
class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    cycle =models.CharField(max_length=10, default='')
    frequency = models.IntegerField(default=0)
    installLocation = models.CharField(max_length=10, default='')
    equipmentId = models.ForeignKey(Equlpment, on_delete=models.CASCADE)
    physicalSensorId = models.ForeignKey(Physical_Sensor_manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
