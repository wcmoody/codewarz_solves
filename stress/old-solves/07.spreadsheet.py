#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    header = lines[0]
    spread = {}
    for column in header.split(','):
        spread[column] = []
    for line in lines[1:]:
        if len(line) == 0: continue
        for col,value in zip(header.split(','),line.split(',')):
            spread[col].append(value)
    totals = {}
    for column in header.split(','):
        valids = [x for x in spread[column] if isfloat(x)]
        totals[column] = sum([float(v) for v in valids])
    print header
    output = []
    for column in header.split(','):
        if int(totals[column]) == totals[column]:
            output.append(str(int(totals[column])))
        else:
            output.append(str(totals[column]))
    print ','.join(output)
