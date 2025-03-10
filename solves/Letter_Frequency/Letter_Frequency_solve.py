#!/usr/bin/env python
import sys
import string

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    data = myinput.read()
    letters = []
    counts = []
    for l in data:
        if l in string.ascii_letters:
            letter = l.lower()
            if letter in letters:
                counts[letters.index(letter)] += 1
            else:
                letters.append(letter)
                counts.append(1)
    print "letters:" + ', '.join(["{:>4s}".format(l) for l in letters])
    print "counts: " + ', '.join(["{:>4d}".format(c) for c in counts])
