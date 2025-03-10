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
        for word in line.split(' '):
            if len(word) > 3:
                ans.append(word[1] + word[0] + word[2:-2] + word[-1] + \
                        word[-2])
            else:
                ans.append(word)
        print ' '.join(ans)
