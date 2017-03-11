#!/usr/bin/env python
import sys
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

patt = re.compile(r'([a-zA-Z]*)')

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    numbers = eval(lines[0])
    match = patt.findall(lines[1])
    if match:
        firsthalf = match[0]
    secondhalf = ""
    for letter, value in zip(firsthalf[::-1],numbers[::-1]):
        secondhalf += chr(value - ord(letter))

    print firsthalf + secondhalf
