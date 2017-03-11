#!/usr/bin/env python
import sys
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

addresses = {}
basefile = open(sys.argv[1],'rt')
filename = basefile.read().strip()
basefile.close()

with open(filename,'r') as myinput:
    for line in myinput:
        matches = pattern.findall(line.strip())
        if matches:
            invalid = False
            address = matches[0]
            for octet in address.split('.'):
                if int(octet) > 255:
                    invalid = True
            if not invalid:
                if address not in addresses.keys():
                    addresses[address]=0
                addresses[address] += 1

alladdrs = []
for addr, cnt in addresses.items():
    newDict={}
    newDict['address'] = addr
    newDict['count'] = cnt
    alladdrs.append(newDict)

def value(ipaddr):
    binary = 0
    octets = ipaddr.split('.')
    for i,o in enumerate(octets):
        binary += int(o) << (8*(3-i))
    return binary

alladdrs = sorted(alladdrs,key=lambda a: value(a['address']), reverse=True)
alladdrs = sorted(alladdrs,key=lambda a: a['count'], reverse=True)

for sa in alladdrs:
		print "{:>15s}".format(sa['address']) + ": " + "*"*sa['count'] + " (%d)"%sa['count']



