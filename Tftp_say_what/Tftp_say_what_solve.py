#!/usr/bin/env python
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

pcap = rdpcap(sys.argv[1])
msg = ''
i = 0
flag = ''
for pkt in pcap:
    if Ether in pkt:
        srcmac = ''.join([b for b in pkt[Ether].src.split(':')])
        binsrcmac = bin(int(srcmac,16))[2:]
        srcmac = '0' * (48-len(binsrcmac)) + binsrcmac
        flag += chr(int(srcmac[-7:],2))
        #print " ".join(srcmac)
        #print "{:>48s}".format(bin(int(srcmac,16))[2:])

print \
flag.decode('base64').decode('base64').decode('base64').decode('base64').decode('rot13')
