#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for index in range(0,len(lines),2):
        output = []
        line1 = lines[index]
        if len(line1) == 0: continue
        line2 = lines[index+1]
        for x,y in zip(line1,line2):
            output.append((x+y).decode('hex'))
        print ''.join(output)
