#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        output = []
        if len(line) == 0: continue
        for word in line.split(' '):
            if len(word) % 2 == 1:
                output.append(word[1::2]+word[::-2])
            else:
                output.append(word[1::2]+word[-2::-2])
        print "twisted:",line
        print "plain  :", ' '.join(output)

