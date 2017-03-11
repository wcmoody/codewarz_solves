#!/usr/bin/env python
import sys
import socket
import re
import struct
from string import digits

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

def int2ip(addr):
    address = int(addr.group(0))
    return socket.inet_ntoa(struct.pack("!I", address))

numpat = re.compile("^\d{6,}$")

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

for line in data:
    output = []
    for word in line.split(' '):
        output.append(numpat.sub(int2ip,word))
    print ' '.join(output)


