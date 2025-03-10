#!/usr/bin/env python
import sys
import string

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

def rotUpper(char,i):
    return string.uppercase[(string.uppercase.index(char)+i) % 26]

def rotLower(char,i):
    return string.lowercase[(string.lowercase.index(char)+i) % 26]


def caesar(str1,i):
    answer = ""
    for c in str1:
        if c in string.uppercase:
            answer += rotUpper(c,i)
        elif c in string.lowercase:
            answer += rotLower(c,i)
        else:
            answer += c
    return answer

def removePunc(str1):
    return "".join([c for c in str1 if c in string.uppercase + string.lowercase])
    

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        sentenance = []
        if len(line) == 0: continue
        for i, word in enumerate(line.split()):
                #if removePunc(caesar(word,i)).lower() in words:
            sentenance.append(caesar(word,-1*(i%26)))
        print ' '.join(sentenance)

