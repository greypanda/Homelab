import requests
import json
import os

obj =  os.scandir('.')
for net in obj:
    if net.name.startswith('172'):

        with open(net,'r') as data:
            jdata = data.read()

            print(jdata)

#response = requests.get(f'http://localhost:8000/api/1/device_detail/172.16.0.2')
#print(response)
#jdata = '{"hostname": "hass.pandavista.org", "hostip": "172.16.0.60"}'
            response = requests.post('http://localhost:8000/api/1/device_add/', json=jdata,timeout=5)
            print(response)