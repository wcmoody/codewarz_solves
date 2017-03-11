#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
		for line in myinput:
				x, y = [int(i) for i in line.strip().split()]
				low = min(x,y)
				high = max(x,y)
				nums = [str(n) for n in range(low,high+1) if (n%7==0) and (n%5 != 0)]
				print ",".join(nums)
