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
        letters = line.split('0x')
        for letter in letters:
            if len(letter)>0:
                output.append(chr(int(math.sqrt(int(letter,16)))))
        print ''.join(output)
