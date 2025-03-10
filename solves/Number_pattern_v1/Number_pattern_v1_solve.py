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
    for line in lines:
        ans = []
        if len(line) == 0: continue
        base = int(line)
        for x in [3, 1,3,3,7]:
            base += x
            ans.append(str(base))
        print ' '.join(ans)

