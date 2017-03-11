#!/usr/bin/env python
import sys
import gzip

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    data = myinput.read()

d = "\x1f\x8b\x08" + data[3:]

with open('/tmp/madeye_out.gz','w') as f:
    f.write(d)

with gzip.open('/tmp/madeye_out.gz','rb') as f:
    flag = f.read()

print flag.strip()


