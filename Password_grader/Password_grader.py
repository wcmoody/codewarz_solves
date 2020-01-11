#!/usr/bin/env python
import sys
from string import uppercase, lowercase, digits, punctuation

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


def lengthcheck(password):
    return 20 >= len(password) >= 8 
def lowercheck(password):
    return any(c in lowercase for c in password)
def uppercheck(password):
    return any(c in uppercase for c in password)
def specialcheck(password):
    return any(c in punctuation for c in password)
def numbercheck(password):
    return any(c in digits for c in password)




with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        fail = 0
        if not lengthcheck(line): fail += 1
        if not lowercheck(line): fail += 1
        if not uppercheck(line): fail += 1
        if not specialcheck(line): fail += 1
        if not numbercheck(line): fail += 1
        if fail == 0:
            response = "Passed all checks!"
        else:
            response = "Failed %d check" % fail
        if fail > 1:
            response +='s'

        output = "Password: (%s) %s  Status: %s"
        ll = str(len(line))
        if len(ll) == 1: ll = "0" + ll
        print output % (ll, (line+20*' ')[:20], response)

