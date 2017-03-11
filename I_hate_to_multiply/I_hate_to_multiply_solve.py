#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    for line in myinput.readlines():
        topnum = int(line.strip())
        for row in range(1,topnum+1):
            for col in range(1,row):
                print "{:<10s}".format("%dx%d=%d" % (row,col,row*col)).lstrip(),
            print"{}".format("%dx%d=%d" % (row,row,row*row))
