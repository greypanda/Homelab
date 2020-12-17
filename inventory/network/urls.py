from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import devices, devices_detail


urlpatterns = [
    path('api/1/devices/', devices, name="devices"),
    path('api/1/devices_detail/<int:pk>', devices_detail, name="devices_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)