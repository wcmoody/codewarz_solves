#!/usr/bin/env python
import sys
from hashlib import sha1
import os

usage = "%s <directory>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

subdirectories = os.walk(sys.argv[1])

filehashes = []

for entry in subdirectories:
    path, subd, files = entry
    for f in files:
        with open(path+'/'+f) as of:
            data = of.read()
            h = sha1(data).hexdigest()
            filehashes.append((f,h))

sortfh = sorted(filehashes)
superhash = ''.join([fh[1] for fh in sortfh])

print sha1(superhash).hexdigest()
    
