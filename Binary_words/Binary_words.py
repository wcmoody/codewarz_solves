#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

def convert(w):
	 val = 0
	 for c in w:
		 val += int(bin(ord(c))[2:])
	 return str(val)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

#words = "Usenet supercomputers try occasional passwords".split(' ')

data = {}

for w in words:
    key = convert(w)
    data[key] = w

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        answer = []
        if len(line) == 0: continue
        for value in line.split(' '):
            answer.append(data[value])
        print " ".join(answer)
			

        



