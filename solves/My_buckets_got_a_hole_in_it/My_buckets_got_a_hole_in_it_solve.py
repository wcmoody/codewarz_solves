#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

tens = {}
with open(sys.argv[1],'r') as myinput:
    for line in myinput:
        value = int(line.strip())
        index = value / 10
        if index not in tens.keys():
            tens[index]=0
        tens[index]+=1

for i in range(max(tens.keys())+1):
    if i not in tens.keys():
        tens[i] = 0
print ''.join([str(x) for x in tens.values()])
