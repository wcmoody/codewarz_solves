#!/usr/bin/env python
import sys
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

#thanks stack overflow
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        vals = line.split(' ')
        if len(vals) != 4: continue
        if not all([is_number(w) for w in line.split()]): continue
        
        if all([vals[0] == y for y in vals[1:]]): m = 4
        else: m = 1
        
        vals = [float(x) for x in line.split(' ')]
        ans = sum(vals) * m
        
        #if int(ans) == ans:
        if '.' not in line: 
            print int(ans)
        else: print ans
