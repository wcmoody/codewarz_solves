#!/usr/bin/env python
import sys
import math

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        output = []
        if len(line) == 0: continue
        for i in range(0,len(line),2):
            output.append(chr(int(line[i:i+2],16)/2))
        print ''.join(output)
