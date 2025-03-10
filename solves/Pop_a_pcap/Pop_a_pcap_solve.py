#!/usr/bin/env python
import sys
from scapy.all import *
import gzip
import StringIO
import re

patt = re.compile(r'Welcome to your home, (.*)! It.*(CTD{.*})')

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

packets = rdpcap(sys.argv[1])

for packet in packets:
    if packet[IP].sport == 80 and Raw in packet:
        if "Content-Encoding" in packet[Raw].load:
            z =  packet[Raw].load.split("Content-Type: text/html\r\n\r\n")[1]
            fileStream = StringIO.StringIO(z)
            gzipper = gzip.GzipFile(fileobj=fileStream)
            data = gzipper.read()
            #if "Welcome to your home" in data:
            matches = patt.findall(data)
            if matches: print matches[0][0], matches[0][1]
