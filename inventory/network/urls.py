from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import devices, device_detail,device_add


urlpatterns = [
    path('api/1/devices/', devices, name="devices"),
    path('api/1/device_add/', device_add, name="device_add"),
    path('api/1/device_detail/<pk>', device_detail, name="device_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)