#!/usr/bin/env python
import sys
from itertools import permutations as perms

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


ops = []
for op in perms(['+','-','/','*'],4):
    ops.append(op)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        results = {}
        if len(line) == 0: continue
        base = line.replace(',', " %s ")
        for perm in ops:
            equation = base % perm
            results[eval(equation)] = perm 
        highest = max(results.keys())
        print "{:10.2f} ('{}', '{}', '{}', '{}')".format(highest, *results[highest])
