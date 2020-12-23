from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Device
from .serializers import DeviceSerializer
from django.http import HttpResponseNotFound

# Get a list of all devices
@api_view(['GET',])
def devices(request, format=None):
   
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

# get a single device
@api_view(['GET',])
def device_detail(request, pk, format=None):
    
    
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        device = None
    
    if device == None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DeviceSerializer(device)
    return Response(serializer.data)

# add a device to DB
@api_view(['POST',])
def device_add(request):
    device_data = json.loads(JSONParser().parse(request))
    device_serializer = DeviceSerializer(data=device_data)
   
    if device_serializer.is_valid():
        device_serializer.save() # save to db
        return JsonResponse(device_serializer.data, status=status.HTTP_201_CREATED)
    print(f'Data: {device_data} error: {device_serializer.errors}')
    return JsonResponse(device_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update a device   
# # ************ needs a lot of work 
@api_view(['PUT',])
def device_update(request, pk ,format=None):
    
    #print(f"finding { pk }")
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        print('oopsie')
        return Response(status=status.HTTP_404_NOT_FOUND)  

    # compare new with stored data
    newd = json.loads(request.data)
    #print(f'New data: {newd}')
    #print(f'Old data: { device} ')
    #print(f"Host name {newd['hostname']}")
    if not device.hostname == newd['hostname']:
        return Response("host name mismatch",status=HTTP_422_UNPROCESSABLE_ENTITY)
    elif not device.macaddress == newd['macaddress']:
        return Response("mac address mismatch",status=HTTP_422_UNPROCESSABLE_ENTITY)
    #newd.pop('hostip')
    
    #print(f'Replace data: {newd}')
    


    
    
    serializer = DeviceSerializer(data=newd)
  
    serializer.is_valid()
    print(f'Valid: {serializer.errors}')
    print(f'Data: { serializer.data}')
    if serializer.is_valid():
        
        print(f"Updating { serializer.data }")
        serializer.update(serializer,serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

