import nmap                         # import nmap.py module
import pprint
import json
import requests
import sys
import os
try:
    nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
    #nm.require_root()
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(1)
     
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

for subnet in range(8):
    hostnet = '172.16.' + str(subnet) + '.0/24'
    #hostnet = '172.16.0.2'
    print('----------------------------------------------------')
    print(f'Scanning {hostnet} ')
    pp = pprint.PrettyPrinter(indent=4)
    #nm.scan(hosts=hostnet, arguments='-n  -sP -PE -PA21,23,80,3389')
    #nm.scan(hostnet,sudo=True,arguments='-O')
    nm.scan(hostnet,sudo=True,arguments="-O -p22-1023,1883,1884,5000,5666")

    hosts = nm.all_hosts()
    # create a dictionary for each host
    # convert the dict to a json document
    # submit the document to the Django inventory API

    
    for h in nm.all_hosts():
        
        hostd = {}
        print("-----------Scanner--------------------")
        hostd["hostip"] = nm[h]['addresses']['ipv4']
        try:
            hostd['macaddress'] = nm[h]['addresses']['mac']
        except:
            hostd['macaddress'] = "none"
        try:
            mactokens = hostd['macaddress'].split(":")
            mac0 = mactokens[0]
            mact = mac0[1]
            if mact in ["2","6","A","E"]:
                hostd['vendor'] = "Local"
            else:
                hostd['vendor'] = nm[h]['vendor'][hostd['macaddress']]
        except:
            hostd['vendor'] = "FAIL"
        try:
            if nm[h]['hostnames'][0]['type'] == 'PTR':
                hostd["hostname"] = nm[h]['hostnames'][0]['name']
            else:
                hostd["hostname"] = "None"
        except:
            hostd["hostname"] = "none"
        
        
        if 'osmatch' in nm[h]:
            for osmatch in nm[h]['osmatch']:
                hostd['osname'] = osmatch['name']
            
                if 'osclass' in osmatch:
                    for osclass in osmatch['osclass']:
                        hostd['ostype'] = osclass['type']
                        hostd['osvendor'] = osclass['vendor']
                        hostd['osfamily'] = osclass['osfamily']
                        hostd['osgen'] = osclass['osgen']
                

        ports = ""
        for proto in nm[h].all_protocols():
        
            lport = list(nm[h][proto].keys())
            lport.sort()
            for port in lport:
            
                if nm[h][proto][port]['state'] == 'open':
                    ports += str(port) + ","

        hostd['ports'] =  ports     
        response = requests.post('http://localhost:8000/api/1/device_add/', json=hostd,timeout=5)
        print(f'Response:{response.status_code}, Data:{ response.content}')