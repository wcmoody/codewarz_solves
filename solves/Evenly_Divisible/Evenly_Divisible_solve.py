#!/usr/bin/env python

import sys
import re
import numpy as np
from decimal import Decimal

usage = "usage %s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

intint = re.compile(r'(-?\d+) (-?\d+)')
intflt = re.compile(r'(-?\d+) (-?\d*\.\d*)')
fltint = re.compile(r'(-?\d*\.\d*) (-?\d+)')
fltflt = re.compile(r'(-?\d*.\d*) (-?\d*\.\d*)')

def iswhole(number):
    if int(number) == number:
        return True
    else:
        return False

with open(sys.argv[1],'r') as myinput:
    answers = []
    lines= myinput.read().split('\n')
    for data in lines:
        if len(data) == 0: continue
        matches = intint.match(data)
        if matches:
            x = abs(int(matches.group(1)))
            y = abs(int(matches.group(2)))
        else:
            matches = intflt.match(data)
            if matches:
                x = abs(int(matches.group(1)))
                y = abs(Decimal(matches.group(2)))
            else:
                matches = fltint.match(data)
                if matches:
                    x = abs(Decimal(matches.group(1)))
                    y = abs(int(matches.group(2)))
                else:
                    matches = fltflt.match(data)
                    if matches:
                        x = abs(Decimal(matches.group(1)))
                        y = abs(Decimal(matches.group(2)))
                    else: continue
        vals = np.arange(x, y+1, x)
        if len([v for v in vals.tolist() if iswhole(v)]) > 0:
            answers.append('\n'.join([str(int(v)) for v in vals.tolist() if iswhole(v)]))
    print '\n\n'.join(answers)
