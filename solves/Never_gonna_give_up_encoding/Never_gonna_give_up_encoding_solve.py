#!/usr/bin/env python
import sys
import string

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

#dictionaryfile = open('/tmp/american-english','rt')
dictionaryfile = open('/usr/share/dict/american-english','rt')

words = dictionaryfile.read().split('\n')

def getmiddle(stry):
    if len(stry) % 2 == 1:
        left = right = len(stry)/2
    else:
        left = len(stry)/2 -1
        right = len(stry)/2
    strings = []
    for i in range(0,len(stry)/2):
        word = stry[left-i:right+i+1]
        if word.lower() in words:
            strings.append(word)
    return strings




with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    answer = []
    foundword = False
    for line in lines:
        if len(line) == 0: continue
        candidates = getmiddle(line)
        answer.append(sorted(candidates,key = lambda c: len(c),
            reverse=True)[0])
    print ' '.join(answer)
