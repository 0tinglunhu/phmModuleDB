from rest_framework import serializers
from .models import Account, Field, Machine, Equlpment, Sensor, Physical_Sensor_manager

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Account
        #fields=('id', 'username', 'password', 'firstName', 'lastName', 'permission', 'userStatus')
        fields='__all__'

class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Field
        #fields=('id', 'name', 'buildingName', 'floor')
        fields='__all__'

class MachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Machine
        #fields=('id', 'name', 'brand', 'model', 'power', 'voltage', 'electric', 'photo', 'fieldId')
        fields='__all__'

class EqulpmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Equlpment
        #fields=('id', 'name', 'brand', 'model', 'power', 'material', 'frequencyType', 'rotationalSpeed', 'fladeCount', 'photo', 'machineId')
        fields='__all__'

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Sensor
        #fields=('id', 'cycle', 'frequency', 'installLocation', 'equipmentId', 'physicalSensorId')
        fields='__all__'

class PhysicalSensorManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Physical_Sensor_manager
        #fields=('id', 'serialNumber', 'name', 'model', 'brand', 'battery', 'wifi', 'cycle', 'frequency', 'onlineTime', 'lastUploadDataTime')
        fields='__all__'