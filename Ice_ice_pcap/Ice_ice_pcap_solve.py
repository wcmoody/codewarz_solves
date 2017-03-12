#!/usr/bin/env python
import sys
from scapy.all import *

usage = "%s <text with path to pcap>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)
path = open(sys.argv[1]).read().strip()
a = rdpcap(path)

sessions = a.sessions()

for packets in sessions.values():
    for packet in packets:
        if packet[TCP].dport == 443 and len(packet[TCP].payload) > 1:
            print str(packet[TCP].payload).lstrip(),
