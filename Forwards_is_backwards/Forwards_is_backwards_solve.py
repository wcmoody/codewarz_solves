#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    for line in myinput:
        word = line.strip()
        if word == word[::-1]:
            print "True"
        else: print "False"
