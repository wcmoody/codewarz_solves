#!/usr/bin/env python

import sys

usage = "usage: %s <input_file>"

if len(sys.argv) < 2:
    exit(usage % sys.argv[0])

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

header = data[0]
columns = header.split(',')
if len(columns) < 4:
    exit("..columns....")

car, gals, start, stop = [-1 for i in range(4)]
for i, col in enumerate(columns):
    if "car" in col:
        car = i
    if "start" in col:
        start = i
    if "stop" in col:
        stop = i
    if "gallon" in col:
        gals = i

if any([x == -1 for x in [car,start,stop,gals]]):
    exit("..any....")
if sum([car,start,stop,gals]) != 6:
    exit("..sum....")

for line in data[1:]:
    if len(line) < 4: continue
    #print line
    values = line.split(',')
    if len(values) < 4:
        exit("......")
    start_ = float(values[start])
    stop_ = float(values[stop])
    car_ = values[car]
    gals_ = float(values[gals])
    mpg = (stop_ - start_) / gals_ 
    print "{:>10} {:5.2f}".format(car_, mpg)




