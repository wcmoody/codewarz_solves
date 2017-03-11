#!/usr/bin/env python
import sys
from collections import OrderedDict

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        tempdict = eval(line)
        mydict = {}
        for k,v in tempdict.items():
            mydict[int(k)] = v
        newdict = OrderedDict(sorted(mydict.items()))
        words = ' '.join(newdict.values()).replace(' \n ','\n')
        print words.strip()
        
