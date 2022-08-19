#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AccountSerializer, FieldSerializer, MachineSerializer, EqulpmentSerializer, SensorSerializer, PhysicalSensorManagerSerializer
from .models import Account, Field, Machine, Equlpment, Sensor, Physical_Sensor_manager
from .filters import AccountFilter

# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #filter_class = AccountFilter
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['username', 'firstName', 'lastName', 'permission', 'userStatus']
    filterset_fields = '__all__'

class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class EqulpmentViewSet(viewsets.ModelViewSet):
    queryset = Equlpment.objects.all()
    serializer_class = EqulpmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class PhysicalSensorManagerViewSet(viewsets.ModelViewSet):
    queryset = Physical_Sensor_manager.objects.all()
    serializer_class = PhysicalSensorManagerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
