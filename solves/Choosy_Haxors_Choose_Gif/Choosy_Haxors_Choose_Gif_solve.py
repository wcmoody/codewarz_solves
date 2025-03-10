#!/usr/bin/env python
from PIL import Image
import re
from PIL import ImageSequence
import sys

usage = "%s <input_file>" % sys.argv[0]

patt = re.compile('(CWN\{[^\}]*\})')
flag = "CWN{al_gores_internet_ftw}"
if len(sys.argv) < 2:
    exit(usage)

image = Image.open(sys.argv[1])

frames = [frame.copy() for frame in ImageSequence.Iterator(image)]

f1 = ""
f2 = ""

for i, frame in enumerate(frames):
    im = frame.load()
    for y in range(0, image.size[1],10):
        for x in range(0, image.size[0],10):
            if i == 0: f1+= str(im[x,y])
            if i == 1: f2+= str(im[x,y])
msg = ''
for i in range(0,len(f1),8):
    msg += chr(int(f1[i:i+8],2))
    msg += chr(int(f2[i:i+8],2))

print msg


