#!/usr/bin/env python
import sys
import re
from hashlib import md5
import operator

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

patt = re.compile(r'[a-f0-9]{32}')

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

answers = {}

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        hashes = patt.findall(line)
        for myhash in hashes:
            for word in words:
                if md5(word+'.exe').hexdigest() == myhash:
                    #print "%s - %s.exe" % (myhash, word)
                    answers[word]= myhash
                    break

for key in sorted(answers):
    print "%s - %s.exe" % (answers[key], key)

#sorted_answers = sorted(answers.items(), key=operator.itemgetter(1))
#for w,h in sorted_answers:
#    print "%s - %s.exe" % (h,w)
