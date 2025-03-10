#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

def convert(str1):
    if str1[:2] == '0x':
        return int(str1,16)
    if str1[:2] == '0b':
        return int(str1,2)
    if str1[0] == '0':
        return int(str1,8)
    else: return int(str1)


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        values = line.split(' ')
        answer = ""
        for value in values:
            answer += chr(convert(value))
        print answer,
