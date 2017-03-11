#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
    exit(".....")

with open(sys.argv[1]) as f:
    cipher = f.read().strip()

#flag = """LoCk SEcReTs
#aRe dAngeRoUs"""

#cipher = "ad d5 n cd 4 88 r a2 86 a6 8a bc e 9e 86 a6 4 a4 j d3 aa a6 86 d5 8c bc"
cipher = cipher.split(' ')

def encrypt(char, b=10):
    total = ord(char)
    total += total / 16 * b + total % 16
    if char in "jklmno":
        total += 27
    if char in "JKLMNO":
        total += 45
    if total in range(0x20,0x80):
        return chr(total)
    if char == '\n':
        return 'e'
    else:
        return hex(total)[2:]


mydict = {}
myletters = " abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
for l in myletters:
    mydict[encrypt(l)] = l

print "".join(mydict[x] for x in cipher)

