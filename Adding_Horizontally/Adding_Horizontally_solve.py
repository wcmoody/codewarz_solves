#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    with open('/usr/share/dict/american-english','r') as thedict:
        words = thedict.read().split('\n')
except:
    with open('./american-english','r') as thedict:
        words = thedict.read().split('\n')


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    lines = [l for l in lines if len(l) > 0]
    numbers = []
    for i in range(0,len(lines)/2):
        numbers.append(int(lines[i]) + int(lines[len(lines)-1-i]))
    if len(lines) % 2 == 1:
        numbers.append(int(lines[len(lines)/2]))
    print ', '.join([str(n) for n in numbers])



