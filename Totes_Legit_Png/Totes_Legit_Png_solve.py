#!/usr/bin/env python
import sys
from PIL import Image
import re

import re
flagpat = re.compile('CWN{[^}]+?}')

usage = "%s <input_file>" % sys.argv[0]

patt = re.compile('(CWN\{[^\}]*\})')

if len(sys.argv) < 2:
    exit(usage)

image = Image.open(sys.argv[1])
im = image.load()

sumxy = []
for x in range(image.size[0]):
    for y in range(image.size[1]):
        total = im[x,y][0] + im[x,y][1] + im[x,y][2]
        sumxy.append(total)

#sumyx = []
#for y in range(image.size[1]):
#    for x in range(image.size[0]):
#        total = im[x,y][0] + im[x,y][1] + im[x,y][2]
#        sumyx.append(total)

msgxy = ''.join([chr(s) for s in sumxy])
#msgyx = ''.join([chr(s) for s in sumyx])

print flagpat.findall(msgxy)[0]

"""
from collections import Counter
c = Counter()
c.update(sumxy[:800])
print len(c.keys())
for i in range(min(sumxy),max(sumxy)):
    print chr(i), c[i] * '*'
"""
