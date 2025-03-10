#!/usr/bin/env python
import sys
import operator
import string

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

populars = ["{0:0>5}".format(i) for i in range(0,100000)]


def xor5 (key, cipher):
    output = ''
    for i in range(0,len(cipher),5):
        for c,k in zip(cipher[i:i+5],key):
            output += chr(ord(c) ^ ord(k))
    return output

def measure(candidates):
    count = 0
    for w in candidates:
        if w in words:
            count +=1
    return float(count)/len(candidates)

with open(sys.argv[1],'r') as myinput:
    outputs = []
    lines = myinput.read().split('\n')
    for data in lines:
        best = ('',0.0)
        for key in populars:
            candidate = xor5(key,data) 
            ws = candidate.split(' ')
            result = measure(ws)
            if result > best[1]:
                best = (candidate,result)
        outputs.append(best[0])
    print "decrypted:",
    print '\n'.join(outputs)

