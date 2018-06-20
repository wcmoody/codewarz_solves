#!/usr/bin/env python
import sys
from scapy.all import *

pcap = rdpcap(sys.argv[1])
msg = ''
for pkt in pcap:
    if IP in pkt and pkt[IP].ttl not in [16,64,128]:
            msg += chr(pkt[IP].ttl)
print msg.decode('base64').decode('rot13')

