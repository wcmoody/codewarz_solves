#!/usr/bin/env python3
import sys
import ipaddress

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        network, gateway = line.split(' ')
        addr, cidr = network.split('/')
        thenetwork = ipaddress.ip_network(network)
        print("Network: "+addr)
        print("Total usable IP's: "+str(2**(32-int(cidr))-2))
        ur = "Usable range: "
        hosts = []
        for h in thenetwork.hosts():
            hosts.append(h)
        first = hosts[0]
        last = hosts[-1]
        fos = str(first).split('.')
        los = str(last).split('.')
        lasts = []
        for f,l in zip(fos,los):
            if f!=l:
                lasts.append(l)
        lastprint = '.'.join(lasts)
        ur += str(first) + "-" + lastprint
        print(ur)
        print("Broadcast Address: " + str(thenetwork.broadcast_address))
        gip = ipaddress.ip_address(gateway)
        if gip in hosts: 
            print("Gateway Address: " + gateway)
        else:
            print("Gateway Address: Invalid")
        print()




