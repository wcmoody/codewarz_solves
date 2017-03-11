#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

output = ''
with open(sys.argv[1],'r') as myinput:
		for line in myinput:
				for byte in line.strip().split(' '):
					output += byte.decode('hex')
print output
					 
