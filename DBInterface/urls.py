from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'Account', views.AccountViewSet)
router.register(r'Field', views.FieldViewSet)
router.register(r'Machine', views.MachineViewSet)
router.register(r'Equipment', views.EqulpmentViewSet)
router.register(r'Sensor', views.SensorViewSet)
router.register(r'Physical_Sensor_manager', views.PhysicalSensorManagerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]
