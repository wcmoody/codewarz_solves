#!/usr/bin/env python
import sys
from itertools import product
import hashlib
import string

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

chars = string.lowercase+ string.digits + string.punctuation + string.whitespace 

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line)==0: continue
        mystery, sha1hash = line.split('.',1)
        mystery = mystery.replace('_','%s')
        thehash = sha1hash.split(':')[1]
        for combo in product(chars,repeat = 4):
            if hashlib.sha1(mystery % combo).hexdigest() == thehash:
                print mystery%combo
                break
