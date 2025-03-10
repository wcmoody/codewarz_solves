#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

import string
countthese = string.digits + string.letters + ' '

with open(sys.argv[1],'r') as myinput:
    stats = {}
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        for C in line:
            c = C.lower()
            if c in countthese:
                if c not in stats.keys():
                    stats[c] = 0
                stats[c] += 1

total = sum(stats.values())

for k,v in stats.items():
    stats[k] = total - v

import operator
sorted_letters = sorted(stats.items(), key=lambda x: (x[1], x[0]))
for k in sorted_letters:

    print "'%s' %0.2f%s" % (k[0], 100 * (1 - (k[1]/float(total))), '%')

