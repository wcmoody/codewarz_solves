#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        known = "RCN{not_your_moms_rot13}"
        print("Letter\tC\tK\tCompare")
        for c,k in zip(line,known):
            print("%s\t%s\t%s\t%s" % (k, hex(ord(c)),hex(ord(k)),hex(ord(c)^ord(k))))
