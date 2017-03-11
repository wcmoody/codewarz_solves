#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
		for line in myinput:
				try:
						if '.' not in line:
								data = [int(x) for x in line.strip().split(' ')]
								if len(data) ==2: print sum(data)
						else:
								data = [float(x) for x in line.strip().split(' ')]
								if len(data) ==2: print sum(data)

				except:
						pass
