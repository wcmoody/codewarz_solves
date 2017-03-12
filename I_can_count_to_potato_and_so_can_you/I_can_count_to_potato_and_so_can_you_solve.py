#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    for line in myinput:
        base, rest = line.strip().split(' ',2)
        vals = [int(v) for v in rest.split(',')]
        base = int(base)
#                               print "orig:",base, vals
        newVals = vals[base:] + vals[:base]
#                               print "new list:",newVals
#                               print "target:",vals[base-1]
        for nv in newVals:
#                                               print "\t",nv,vals[base-1]
            if nv > vals[base-1]:
                print nv
                break
