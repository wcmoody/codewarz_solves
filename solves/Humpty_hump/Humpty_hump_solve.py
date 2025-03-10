#!/usr/bin/env python
import sys
import os
import subprocess

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

outputs = []

for binary in os.listdir(sys.argv[1]):
    exe = './' + sys.argv[1] + binary
    outputs.append(subprocess.check_output([exe]).strip())

so = sorted(outputs)
so = sorted(so, key=len)

print "CWN{" + '_'.join(so) + "}"    

