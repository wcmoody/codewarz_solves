#!/usr/bin/env python
import sys
import re
import operator

usage = "%s <input_file>" % sys.argv[0]

patt = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

def value(ipaddr):
    binary = 0
    octets = ipaddr.split('.')
    for i,o in enumerate(octets):
        binary += int(o) << (8*(3-i))
    return binary


if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    ips = {}
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        matches = patt.findall(line)
        for match in matches:
            if match not in ips.keys():
                ips[match] = {}
                ips[match]['count'] = 0
            ips[match]['count'] += 1
            ips[match]['valid'] = True
            ips[match]['value'] = value(match)
            ips[match]['addr'] = match
            for octet in match.split('.'):
                if int(octet) > 255:
                    ips[match]['valid'] = False
    allips = [ips.values()]
    sorted_ips = sorted(allips,key=lambda a: a['value'])
    sorted_ips = sorted(allips,key=lambda a: a['count'])

    for si in sorted_ips:
        starcnt = si['count'] % 50 + 1
        print '({}) {}: {} ' + '*'*strcnt

