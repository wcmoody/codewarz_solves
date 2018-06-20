#!/usr/bin/env python
import sys
with open(sys.argv[1],'r') as m: print hex(int(''.join([str(ord(w[-1])%2) for w in m.read().split(' ')]),2))[2:].strip('L').decode('hex')

