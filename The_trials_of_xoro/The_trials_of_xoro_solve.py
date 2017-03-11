#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

plain = "You're weak like your father"


def measure(candidates):
    count = 0
    for w in candidates:
        if w in words:
            count +=1
    return float(count)/len(candidates)


def xor(values):
    result = values[0]
    for v in values[1:]:
        result = chr(ord(result) ^ ord(v))
    return result


def linexor(key, cipher):
    result = ''
    for c in cipher:
        result += xor([key,c])
    return result


keyspace= '0123456789abcdefz'

allkeys = []


for k1 in keyspace:
    allkeys.append(k1)
    for k2 in keyspace:
        allkeys.append(xor([k1,k2]))
        for k3 in keyspace:
            allkeys.append(xor([k1,k2,k3]))
            for k4 in keyspace:
                allkeys.append(xor([k1,k2,k3,k4]))

candidates = set()


with open(sys.argv[1],'r') as myinput:
    cipher = myinput.read()
    for k1 in keyspace:
        cipher = linexor(k1,cipher)
        candidates.add(cipher)
        for k2 in keyspace:
            cipher = linexor(k2,cipher)
            candidates.add(cipher)
            for k3 in keyspace:
                cipher = linexor(k3,cipher)
                candidates.add(cipher)
                for k4 in keyspace:
                    cipher = linexor(k4,cipher)
        candidates.add(cipher)
    best = 0
    highest = 0
    for candidate in candidates:
        m = measure(candidate.split(' '))
        if m > highest:
            best = candidate
            highest = m

    print "decrypted:", best

"""
for key in allkeys:
            candidate = linexor(key,line)
            if candidate == plain:
                print "plain found:", plain
                print "key (hex):", key.encode('hex')
                exit()
"""	
