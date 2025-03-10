#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    with open('/usr/share/dict/american-english','r') as thedict:
        words = thedict.read().split('\n')
except:
    with open('./american-english.txt','r') as thedict:
        words = thedict.read().split('\n')

flag= "This is a test!"

keys = [0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x1]

with open(sys.argv[1],'r') as myinput:
    output = ''
    cipher = myinput.read()
    for i, c in enumerate(cipher):
        output += chr(ord(c) ^ keys[i%len(keys)])
print output


        
