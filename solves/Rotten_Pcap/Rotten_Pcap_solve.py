#!/usr/bin/env python
import sys
from scapy.all import *

usage = "usage: %s <pcap_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

pcap = rdpcap(sys.argv[1])
       
output = []
for packet in pcap:
    if UDP in packet:
        output.append(str(packet[UDP])[-1].decode('rot13'))
        
print ''.join(output)
