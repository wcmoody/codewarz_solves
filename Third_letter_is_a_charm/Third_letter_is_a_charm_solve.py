#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        answer = []
        for word in line.split(' '):
            if len(word)>=3:
                answer.append(word[1:3] + word[0] + word[3:])
            else: answer.append(word)
        print ' '.join(answer)

