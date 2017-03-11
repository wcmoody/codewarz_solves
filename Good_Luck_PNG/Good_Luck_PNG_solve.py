#!/usr/bin/env python
import sys
from PIL import Image
import re

usage = "%s <input_file>" % sys.argv[0]

patt = re.compile('(CWN\{[^\}]*\})')

if len(sys.argv) < 2:
    exit(usage)

image = Image.open(sys.argv[1])
im = image.load()
colors = {} 
blues = []
output = []
for x in range(image.size[0]):
    for y in range(image.size[1]):
        output.append(im[x,y][2])
output = ''.join([chr(x) for x in output])
print patt.findall(output)[0]
