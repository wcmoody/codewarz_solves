#!/usr/bin/env python
import sys
from string import lowercase
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

alpha = {}

tones = "noll, An,  de,  ti,  go,  su,  by,  ra,  me,"
tones += "ni,  ko,  hu,  vy,  la,  po, fy,  ton"

tones = [t.strip() for t in tones.split(',')]
tonespatt = "|".join(tones)

pattern = re.compile(tonespatt)

#answer = "just sound it out!"

with open(sys.argv[1],'r') as myinput:
    answer = ''
    for line in myinput:
        words = line.strip().split()
        for word in words:
            matches = pattern.findall(word)
            charVal = tones.index(matches[0]) * 16 + tones.index(matches[1])
            answer += chr(charVal)
        print answer
