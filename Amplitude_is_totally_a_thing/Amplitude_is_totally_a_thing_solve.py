#!/usr/bin/env python
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from zlib import decompress

pcap = rdpcap(sys.argv[1])
cflag = ''

for pkt in pcap:
    proto = str(pkt)[23].encode('hex')
    cflag += proto

print decompress(cflag.decode('hex'))
