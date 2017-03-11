#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    solution = []
    for line in lines:
        #words = [w for w in line.split(' ') if len(w)>0]
        #for word in words[::-1]:
        #    solution.append(word[::-1])
        solution.append(line[::-1])

print ''.join(solution)

