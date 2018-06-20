#!/usr/bin/env python
import sys
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

addresses = {}

with open(sys.argv[1],'r') as myinput:
    for line in myinput:
        matches = pattern.findall(line.strip())
        for match in matches:
            address = match
            #for octet in address.split('.'):
            #    if int(octet) > 255:
            #        invalid = True
            #if not invalid:
            if address not in addresses.keys():
                addresses[address]=0
            addresses[address] += 1

alladdrs = []
for addr, cnt in addresses.items():
    newDict={}
    newDict['address'] = addr
    newDict['count'] = cnt
    newDict['valid'] = 'True'
    for octet in addr.split('.'):
        if int(octet) > 255:
            newDict['valid'] = 'False'
        if octet[0] == '0' and len(octet) > 1:
            newDict['valid'] = 'False'
    alladdrs.append(newDict)

def value(ipaddr):
    binary = 0
    octets = ipaddr.split('.')
    for i,o in enumerate(octets):
        binary += int(o) << (8*(3-i))
    return binary

alladdrs = sorted(alladdrs,key=lambda a: value(a['address']))
alladdrs = sorted(alladdrs,key=lambda a: a['count'])

for sa in alladdrs:
    starcnt = (sa['count'] / 50) + 1    
    #print "{:>15s}".format(sa['address']) + ": " + "*"*starcnt + " (%d)"%sa['count']
    print "({:03d})".format(sa['count']), "{:>5}:".format(sa['valid']), \
            "{:>15}".format(sa['address']), starcnt*'*'


