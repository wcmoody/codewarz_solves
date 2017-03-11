#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    result = []
    for line in lines:
        if len(line) == 0: continue
        output = []
        for word in line.split(' '):
            if len(word) < 4:
                output.append(word)
            else:
                newword = ''
                newword += word[:len(word)/2][::-1]
                if len(word)%2 == 1:
                    newword += word[len(word)/2]
                newword += word[int(round(len(word)/2.)):][::-1]
                if len(newword)==0: continue
                output.append(newword)
        if len(output) > 1: result.append(' '.join(output))
    print '\n'.join(result)
