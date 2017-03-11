#!/usr/bin/env python
import sys
from string import uppercase, lowercase

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    with open('/usr/share/dict/american-english','r') as thedict:
        words = thedict.read().split('\n')
except:
    with open('./american-english','r') as thedict:
        words = thedict.read().split('\n')

total = 0
with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        for c in line:
            if c in uppercase or c in lowercase:
                total += ord(c)

    print total
