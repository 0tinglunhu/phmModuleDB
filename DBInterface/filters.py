from django_filters import rest_framework as filters
from . models import Account, Field, Machine, Equlpment, Sensor, Physical_Sensor_manager

class AccountFilter(filters.FilterSet):
    class Meta:
        model = Account
        fields = [ 'username', 'firstName', 'lastName', 'permission', 'userStatus']
