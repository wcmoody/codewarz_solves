#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        output = []
        for word in line.split(' '):
            if len(output) == 0 or word != output[-1]:
                output.append(word)
        print ' '.join(output)
