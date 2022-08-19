from django.contrib import admin
from .models import Account, Field, Machine, Equlpment, Sensor, Physical_Sensor_manager

# Register your models here.
admin.site.register(Account)
admin.site.register(Field)
admin.site.register(Machine)
admin.site.register(Equlpment)
admin.site.register(Sensor)
admin.site.register(Physical_Sensor_manager)