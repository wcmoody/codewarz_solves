#!/usr/bin/env python
import sys
from re import compile
import socket
from collections import Counter
import math

usage = "%s <input_file>" % sys.argv[0]

pat = compile("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")


def valid_ip(address):
    try: 
        if address == "0.0.0.0": return False
        socket.inet_aton(address)
        return True
    except:
        return False


if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    data = myinput.read()

matches = pat.findall(data)

if matches:
    ips = [i for i in matches if valid_ip(i)]
    counts = Counter(ips)

    sorted_counts = sorted(counts.items(), key=lambda pair: (pair[1],\
    socket.inet_aton(pair[0])))

    total = sum([v for v in counts.values()])

    print "-------------------------------------"
    print "| Percent | Count |              IP |"
    print "-------------------------------------"


    for k,v in sorted_counts:
        f = float(100*v) / total
        if f> 10.0:
            percent = math.floor(f * 10 ** 3) / 10 ** 3
            print "|  {:6.3f} | {:>5d} | {:>15s} |".format(percent,v,k) 
        else:
            percent = math.floor(f * 10 ** 4) / 10 ** 4
            print "|  {:6.4f} | {:>5d} | {:>15s} |".format(percent,v,k) 

    print "-------------------------------------"
    print "|   Total | {:5d} |                 |".format(total)
    print "-------------------------------------"

        
