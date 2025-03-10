#!/usr/bin/env python
import sys
from scapy.all import *
import re


def value(ipaddr):
    binary = 0
    octets = ipaddr.split('.')
    for i,o in enumerate(octets):
        binary += int(o) << (8*(3-i))
    return binary

patt = re.compile(r'\[(\w+)\]')

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

packets = rdpcap(sys.argv[1])
history = {}
records = {}
for i, packet in enumerate(packets):
    if Raw in packet:
        thismessage = packet[Raw].load
        thisip = packet[IP].src
        match = patt.findall(thismessage)
        if match:
            message = thismessage.split("] ")[1]
            if message in history.keys():
                user = match[0]
                records[user] = history[message] 
                records['server'] = thisip
                del history[message]
        else:
            history[thismessage] = thisip

sorted_results = {}
for k,v in records.items():
    ipval = value(v)
    sorted_results[ipval] = "%s => %s" % (v,k)

for key in sorted(sorted_results.keys()):
    print sorted_results[key]
