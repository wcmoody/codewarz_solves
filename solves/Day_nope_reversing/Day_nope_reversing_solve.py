#!/usr/bin/env python
import sys

usage = "%s <cipher_text>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


cipher = sys.argv[1]

plain = ''

for i, c in enumerate(cipher):
    if i == 7:
        plain += chr(ord(c) -2)
    elif i % 2 == 0:
        plain += chr(ord(c) +1)
    else:
        plain += chr(ord(c) -1)

print plain
