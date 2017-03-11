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
reds = []
blues = []
greens = []

columnbits = ''

for x in range(0,image.size[0],7):
    for y in range(0,image.size[1],7):
        columnbits += str(im[x,y])

rowbits = ''

for y in range(0,image.size[1],7):
    for x in range(0,image.size[0],7):
        rowbits += str(im[x,y])


#rowbits = '000000' + rowbits.replace('1','2').replace('0','1').replace('2','0')
#columnbits = '000000' + columnbits.replace('1','2').replace('0','1').replace('2','0')

columnmsg = ''.join([chr(int(columnbits[i:i+7],2)) for i in \
    range(0,len(columnbits),7)])
rowmsg    = ''.join([chr(int(rowbits[i:i+7],2))    for i in \
    range(0,len(rowbits),   7)])

import re
flagpat = re.compile('CWN{[^}]+}')

colmatch = flagpat.findall(columnmsg)
rowmatch = flagpat.findall(rowmsg)
if len(colmatch) == 1:
    print colmatch[0]
if len(rowmatch) == 1:
    print rowmatch[0]
