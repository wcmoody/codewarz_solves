#!/usr/bin/env python
import sys
import re


usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

myinput = open(sys.argv[1],'r').readlines()
#print len(myinput)

for line in myinput:
    if len(line.strip())==0:
        continue
#       print line.strip()
    myerror = False
    count = 0
    for char in line.strip():
        if char=='0': count += 1
        if char=='1': count -= 1
        if count < 0: myerror = True
    if count == 0 and not myerror:
        print "True"
    else:
        print "False"
