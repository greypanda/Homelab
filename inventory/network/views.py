import json

from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Device
from django.forms.models import model_to_dict
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
# Get a list of all devices

def devices(request):
   
    devices = Device.objects.all()
    device_list = serializers.serialize('json',devices)
    return HttpResponse(device_list,content_type="text/json")

def device_detail(request, pk, format=None):
    
    try:
        device = model_to_dict(Device.objects.get(pk=pk))
        return JsonResponse(device,content_type="text/json",safe=False)
    except Device.DoesNotExist:
        return HttpResponseNotFound()
    


@csrf_exempt
def device_add(request):
   
    device_data = request.body
    jdata = json.loads(device_data)
    if  not jdata.get('hostip'):
        response = HttpResponse()
        response.status_code = 400
        response.content = "Required field host ip missing"
        return response
    if  not jdata.get('macaddress'):
        response = HttpResponse()
        response.status_code = 400
        response.content = "Required field mac address missing"
        return response

    device = Device(
                     hostname = jdata.get("hostname"),
                     hostip = jdata.get("hostip"),
                     macaddress = jdata.get('macaddress'),
                     vendor = jdata.get('vendor','Unknown'),
                     osfamily = jdata.get('osfamily',"None"),
                     osname = jdata.get('osname',"None"),
                     ostype = jdata.get('ostype',""),
                     osvendor = jdata.get('osvendor',"None"),
                     ports = jdata.get('ports',''),
                     location = jdata.get('location',"Unknown"),
                     valid = True,

    )
    device.save()
    
    response = HttpResponse()
    response.status_code = 201
    response.content = "Record created"
    return response


    
   