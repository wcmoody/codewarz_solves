#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

def untitle(w):
    return w[0].lower() + w[1:]

from string import punctuation as punc

def findlongest(wordz):
    thepunc = ''
    if wordz[-1] in punc:
        thepunc = wordz[-1]
        wordz = wordz[:-1]
    for i in range(len(wordz),1,-1):
        if wordz[:i] in words or untitle(wordz[:i]) in words:
            return wordz[:i]+thepunc

def removejunk(wordz):
    thepunc = ''
    if wordz[-1] in punc:
        thepunc = wordz[-1]
        wordz = wordz[:-1]
    return wordz[:-1] + thepunc



with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        outputstr = []
        for w in line.split(' '):
            if len(w) == 0: continue
            longword = removejunk(w)
            if longword:
                outputstr.append(longword)
        print ' '.join(outputstr)

