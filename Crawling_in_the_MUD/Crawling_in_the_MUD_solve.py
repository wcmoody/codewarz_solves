#!/usr/bin/env python
import sys
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

strokes = ['U','u','MH','mh','D','d','SL','sl']
pattern = re.compile('|'.join(strokes))

gains = [2,1,6,3,-2,-1,-6,-3]
vals = {}

for s,g in zip(strokes,gains):
    vals[s] = g

level = 0
with open(sys.argv[1],'r') as myinput:
    for line in myinput:
        matches = pattern.findall(line.strip())
        for match in matches:
            level += vals[match]
print level
