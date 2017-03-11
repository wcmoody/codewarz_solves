#!/usr/bin/env python
import sys
from string import uppercase as uc

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        for word in line.split():
            if (word[0] in uc) and not all([c in uc for c in word[1:]]):
                print word,
        print
