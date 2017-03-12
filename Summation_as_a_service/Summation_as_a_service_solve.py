#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    for line in myinput:
        x, y = [int(i) for i in line.strip().split(' ')]
        high = max(x,y)
        low = min(x,y)
        print sum(range(low,high+1))
