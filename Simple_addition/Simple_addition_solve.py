#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        try:
            a, b = [int(x) for x in line.split(' ')]
        except:
            a, b = [float(x) for x in line.split(' ')]
        print a + b
