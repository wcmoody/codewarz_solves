#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
		for line in myinput:
				items = line.strip().split(' ')
				if len(items) == 0:
						print ''
				sortitems = sorted(items)
				distance = 0
				for item in items:
						distance += abs(sortitems.index(item) - items.index(item))
				if distance != 0: print distance
				else: print ''
