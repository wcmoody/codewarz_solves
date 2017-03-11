#!/usr/bin/env python
import sys
import subprocess

exe = './' + sys.argv[1]
print subprocess.check_output([exe,'6', 'cats', 'in', 'MAH', 'yard'])
