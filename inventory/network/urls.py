from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from network import views

urlpatterns = [
    path('api/1/devices/', views.DeviceList.as_view(), name="devices"),

    path('api/1/devices/<pk>', views.DeviceDetail.as_view(), name="device_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)