#!/usr/bin/env python
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

pcap = rdpcap(sys.argv[1])
msg = ''
for pkt in pcap:
    if IP in pkt and pkt[IP].ttl not in [64]:
        if UDP in pkt and pkt[UDP].dport == 67: 
            msg += chr(pkt[IP].ttl)
print msg.decode('base64').decode('rot13')

