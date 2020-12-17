import nmap                         # import nmap.py module
import pprint
import json

try:
    nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(1)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

for subnet in range(6):
    hostnet = '172.16.' + str(subnet) + '.0/24'
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
        hostd["ipv4"] = nm[h]['addresses']['ipv4']
        try:
            hostd['mac'] = nm[h]['addresses']['mac']
        except:
            hostd['mac'] = "none"
        try:
            mactokens = hostd['mac'].split(":")
            mac0 = mactokens[0]
            mact = mac0[1]
            if mact in ["2","6","A","E"]:
                hostd['macvendor'] = "Local"
            else:
                hostd['macvendor'] = nm[h]['vendor'][hostd['mac']]
        except:
            hostd['nicvendor'] = "none"
        try:
            if nm[h]['hostnames'][0]['type'] == 'PTR':
                hostd["hostname"] = nm[h]['hostnames'][0]['name']
            else:
                hostd["hostname"] = "None"
        except:
            hostd["hostname"] = "none"
        
        
        if 'osmatch' in nm[h]:
            osd = {}
            for osmatch in nm[h]['osmatch']:
                osd['name'] = osmatch['name']
             
                if 'osclass' in osmatch:
                    for osclass in osmatch['osclass']:
                        osd['type'] = osclass['type']
                        osd['vendor'] = osclass['vendor']
                        osd['family'] = osclass['osfamily']
                        osd['osgen'] = osclass['osgen']
                   

            hostd['os'] = osd
        ports = []
        for proto in nm[h].all_protocols():
           
            lport = list(nm[h][proto].keys())
            lport.sort()
            for port in lport:
              
                if nm[h][proto][port]['state'] == 'open':
                    ports.append(port)

        hostd['ports'] = ports    
        pp.pprint(hostd)
        jsond = json.dumps(hostd)
        print(jsond)