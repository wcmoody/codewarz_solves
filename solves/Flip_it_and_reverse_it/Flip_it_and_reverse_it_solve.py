#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    words = []
    for line in lines:
        if len(line) == 0: continue
        for w in line.split(' '):
            words.append(w)
    for i,w in enumerate(words):
        if i%2 == 0:
            print w
        else:
            print w[::-1]

