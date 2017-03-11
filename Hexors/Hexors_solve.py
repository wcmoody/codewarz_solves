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

populars = [chr(x) for x in range(0,256)]
from string import printable
myhex = "0123456789abcdefABCDEF"

def xor(key,line):
    output = ''
    kl = len(key)
    for i in range(0,len(line),kl):
        for c,k in zip(line[i:i+kl],key):
            output += chr(ord(c) ^ ord(k))
    return output

def measure(candidates):
    count = 0
    for i, w in enumerate(candidates):
        if w in words:
            count +=1
        if i > 100 and w<10:
            return False
    if float(count)/len(candidates) > 0.80:
        return True
    else: return False

flag = "Funtimes is an evil challenge writer"

with open(sys.argv[1],'r') as myinput:
    data = myinput.read()
    best = ('',0.0)
    for key in populars:
        candidate = xor(key,data)
        if len(candidate) % 2 ==1 :
            candidate = '0' + candidate
        if all([x in myhex for x in candidate]):
            if all([h in printable for h in candidate.decode('hex')]):
                ws = candidate.decode('hex').split(' ')
                result = measure(ws)
                if result > best[1]:
                    best = (candidate.decode('hex'),result)
    print "decrypted:",
    print best[0] 




