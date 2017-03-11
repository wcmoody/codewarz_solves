#!/usr/bin/env python
import sys
from itertools import permutations

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
        if len(line) == 0: continue
        perms = permutations(line,len(line))
        mywords = set()
        for p in sorted(perms):
            if ''.join(p) in words:
                mywords.add(''.join(p))
            elif ''.join(p).title() in words:
                mywords.add(''.join(p))
        for w in sorted(mywords):
            print w
        

