#!/usr/bin/env python
import sys
from hashlib import sha1, sha256, sha224, sha512, md5, sha384
import os


usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

from hashlib import sha1, sha256, sha224, sha512, md5, sha384

hashlen = {32:md5, 40:sha1, 64:sha256, 56:sha224, 96:sha384, 128:sha512}

victory = "Found the file %s%s with the hash of %s"

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')

files = {} 

for f in os.listdir(sys.argv[2]):
    with open(sys.argv[2] + '/' + f) as ff:
        files[f] = ff.read()

for line in lines:
        if len(line) == 0: continue
        hlen = len(line.strip())
        phash = hashlen[hlen]
        for name, data in files.items():
            if phash(data).hexdigest() == line.strip():
                print victory % (sys.argv[2], name, line.strip())
                break


            
        
