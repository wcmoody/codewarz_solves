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

populars = [chr(x) for x in range(0,255)]


def removepunc(word):
    myword = word
    exclude = set(string.punctuation)
    if len(myword) > 1:
        if myword[-1] in exclude:
            myword =myword[:-1]
        if myword[0] in exclude:
            myword = myword[1:]
    return myword

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

with open(sys.argv[1],'r') as myinput:
    data = myinput.read()
    counts = dict()
    for i in data:
        counts[i] = counts.get(i, 0) + 1
    
    for key in populars:
        print key.encode('hex')
        candidate = "".join([chr(ord(x)^ord(key)) for x in data])
        ws = candidate.split(' ')
        print len(ws)
        if len(ws) < 100: continue
        if measure(ws):
            print "decrypted:",candidate

        #if all(w in words or w.lower() in words or removepunc(w) in words for w in ws[:8]):
        #    break
        

