#!/usr/bin/env python
import sys
import subprocess

exe = './' + sys.argv[1]
print subprocess.check_output([exe,'one', 'two', 'three', 'four', 'five',\
'six']),
