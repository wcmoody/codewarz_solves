#!/usr/bin/env python
import sys
from string import punctuation
from operator import itemgetter

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

totalwords = {}


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        tokens = line.split(' ')
        for token in tokens:
            word = token.strip(punctuation)
            if word in words:
                if word not in totalwords.keys():
                    totalwords[word] = 0
                totalwords[word] += 1

totalwords = [(word, word.lower(), count) for word, count in totalwords.items() ]
top15 = sorted(totalwords, key=itemgetter(1))
top15 = sorted(top15, key=itemgetter(2),reverse=True)[:15]

for word, sw, count in top15:
    print count, word

