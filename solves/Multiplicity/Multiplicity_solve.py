#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        values = line.split(' ')
        values = [float(v) for v in values]
        p = 1
        for v in values:
            p *= v
        #if int(p) == p:
        if '.' not in line:
            print int(p)
        else:
            print p

