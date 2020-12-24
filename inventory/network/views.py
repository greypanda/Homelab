from network.models import Device
from network.serializers import DeviceSerializer
from django.http import Http404

#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status 
from rest_framework import mixins
from rest_framework import generics

class DeviceList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get(self,request, *args,**kwargs):
        return self.list(request,*args,*kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

class DeviceDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    def get(self,request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)

    
