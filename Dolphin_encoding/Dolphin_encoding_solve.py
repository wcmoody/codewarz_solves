#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        answer = ""
        chars = [line[i:i+2] for i in range(0,len(line),2)]
        for i, char in enumerate(chars):
            newchar = hex(int(char,16) - (i%8+1))[2:]
            if len(newchar)==1:
                newchar = "0" + newchar
            flipped = newchar[1] + newchar[0]
            answer += chr(int(flipped,16))
        print answer
