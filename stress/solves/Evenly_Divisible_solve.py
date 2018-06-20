#!/usr/bin/env python
import sys
import re
from decimal import *

usage = "%s <input_file>" % sys.argv[0]


pattern = re.compile(r'\d+\.0*$')
getcontext().prec=100

def isWholeNumber(myfloat):
    strfloat = str(myfloat)
    if '.' not in strfloat:
        return True
    if len(pattern.findall(strfloat)) > 0:
        return True
    else:
        return False

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    for line in myinput:
        output = False
        if len(line.split(' '))!=2: continue
        strx, stry = line.strip().split(' ')
        try:
            x = Decimal(strx)
            y = Decimal(stry)
        except: continue
        #print "case:", strx, stry
        num = abs(x)
        while num <= y:
            if isWholeNumber(num):
                output = True
                print int(num)
            num += abs(x)
        if output: print 
