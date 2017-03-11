#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
	for line in myinput:
		vals = line.strip()[1:-1].split(',')
		if len(vals) % 2 ==0:
			newlist = [int(vals[x]) + int(vals[len(vals)-1-x]) for x in range(len(vals))]
		else:
			firsthalf=[int(vals[x]) + int(vals[len(vals)-1-x]) for x in range(len(vals)/2)] 
			middle = [int(vals[len(vals)/2])]
			newlist = firsthalf + middle + firsthalf[::-1]
		print newlist
				
