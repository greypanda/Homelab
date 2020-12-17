from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer
from django.http import HttpResponseNotFound

@api_view(['GET', 'POST'])
def devices(request, format=None):
    
    if request.method == 'GET': # user requesting data 
        snippets = Device.objects.all()
        print(snippets)
        serializer = DeviceSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # user posting data
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def devices_detail(request, pk, format=None):
    
    if request.method == 'GET': # user requesting data 
        try:
            snippets = Device.objects.get(pk=pk)
        except:
            content = {f'GET failed for PK = {pk}':"404 Not Found"}
            return Response(content,status = status.HTTP_404_NOT_FOUND)
        serializer = DeviceSerializer(snippets, many=False)
        return Response(serializer.data)

    elif request.method == 'POST': # user posting data
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)