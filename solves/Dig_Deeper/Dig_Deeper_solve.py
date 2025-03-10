#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

import re
patt = re.compile('CWN{[^}]+}')
with open(sys.argv[1],'rt') as myinput:
    print patt.findall(myinput.read())[0]
