#!/usr/bin/env python
import sys
import math

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    with open('/usr/share/dict/american-english','r') as thedict:
        words = thedict.read().split('\n')
except:
    with open('./american-english','r') as thedict:
        words = thedict.read().split('\n')


def nck(n,k):
        return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        row, column = [int(i) for i in line.split(' ')]
        print nck(row,column)
        
