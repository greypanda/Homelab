from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
                    'hostname',
                    'hostip',
                    'macaddress',
                    'vendor',
                    'osfamily',
                    'osname',
                    'ostype',
                    'osvendor',
                    'ports',
                    'location',
                    'valid',
                    'discovered',
                    'lastupdate',
                    'lastresponded',
                    'ansible_group',
                    'dns_group',
        )
    