#!/usr/bin/env python3
from collections import defaultdict
from os import system
#import os as linux
try:
    import netifaces
except ModuleNotFoundError as e:
    system("pip install netifaces")
    #linux.system
    import netifaces
try:
    from pyroute2 import IPRoute
except ModuleNotFoundError as e:
    system("pip install pyroute2")
    from pyroute2 import IPRoute

my_gateways =defaultdict(dict)
my_gateways['192.168.58.1']="192.168.58.237/24"
my_gateways['192.168.1.1']="192.168.1.237/24"

def get_gateway():
    gws = netifaces.gateways()
    gws['default']
    return gws['default'][netifaces.AF_INET][0]
def setIpAddr(iface, staticip,gateway):
    system("ip addr flush ens33")
    system(f"ip addr add {staticip} dev {iface}")
    system(f"ip route add default via {gateway}")
def getipfromgateway(gateway):
    return my_gateways[gateway]
gateway = get_gateway()

system("clear")

print("\n")

if(my_gateways.__contains__(gateway)):
    print("Localizacion reconocida.")
    ip= getipfromgateway(gateway)
    print("\n")
    print(f"Asignando IP: {ip}")
    setIpAddr('ens33', ip,gateway)
else:
    print("Localizacion no reconocida.")
    print("Establezco ip por dhcp")

print ("\n")

system("/usr/sbin/ntpdate hora.cica.es > /dev/null 2>&1 && /usr/bin/hwclock -s")
print("La hora actual es:")
system("date")
print("\n")
