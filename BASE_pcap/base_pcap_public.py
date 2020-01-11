#!/usr/bin/env python
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import re

patt = re.compile(r'\\n')

pcap = rdpcap(sys.argv[1])
sessions = pcap.sessions()    

oldflag = ""

for k,v in sessions.items():
    message = ""
    for pkt in v:
        if Raw in pkt: 
            message += pkt[Raw].load.decode('utf-32')
    flag = patt.sub('',message.split(' ')[-1].strip()).decode('base64').decode('base64').decode('base64')
    if flag != oldflag:
        print flag
        oldflag = flag


