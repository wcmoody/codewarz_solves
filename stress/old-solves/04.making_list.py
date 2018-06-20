#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]


if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    thelist = []
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        cleanline = ','.join([x for x in line.split(',') if x.isdigit()])
        if len(cleanline) == 0: continue
        if len(cleanline.split(',')) == 1:
            thelist.append(eval(cleanline))
        elif len(cleanline.split(',')) > 1:
            thelist.append(list(eval(cleanline)))
    print thelist
