#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

bad = 0
good = 0

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        if line.split(' ')[-1] == 'bad': bad += 1
        elif line.split(' ')[-1] == 'good': good += 1

    print "Naughty list has %d people!" % bad
    print "Nice list has %d people!" % good

