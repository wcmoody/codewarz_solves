#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english','r').read().split('\n')

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        outline = []
        for word in line.split(' '):
            if word.lower() in words or word in words:
                outline.append(word)
        print(' '.join(outline))


