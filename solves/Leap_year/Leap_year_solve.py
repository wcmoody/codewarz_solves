#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

years = []

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        dates = line.split(' ')
        for date in dates:
            if '-' in date:
                start,end = date.split('-',1)
                for year in range(int(start),int(end)+1):
                    years.append(year)
            else: years.append(int(date))

sortedyears = sorted(years)

import calendar 

for y in sortedyears:
    print "%d: %r" % (y, calendar.isleap(y))
    
