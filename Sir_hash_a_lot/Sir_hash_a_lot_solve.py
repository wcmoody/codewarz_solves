#!/usr/bin/env python
import sys
from hashlib import sha1, sha256, sha224, sha512, md5, sha384
import string
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

def rotX(mystring, i):
    answer = ''
    for char in mystring:
        if char in string.digits:
            answer += char
        else:
            newchar = chr((ord(char)+i-97)% 26 + 97)
            answer += newchar
    return answer

patt = re.compile('|'.join(string.lowercase))

def mask(mystring):
    answer = re.sub(patt,'_',mystring)
    return answer


hashlen = {32:md5, 40:sha1, 64:sha256, 56:sha224, 96:sha384, 128:sha512}
try:
    dictfile = open('/usr/share/dict/american-english','rt') # uncomment 4 upload
except:
    dictfile = open('./american-english.txt','rt') # remove for upload

dictionary = dictfile.read().split('\n')
#dictionary = ['sir','hash','a','lot','electroencephalograph\'s']
#dictfile.close()


with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        done = False
        w = 0
        if len(line) == 0: continue
        length = len(line)
        if length in hashlen.keys():
            for word in dictionary:
#                print "trying",word
                #w = w + 1
                #for i in range(27):
                #if done: break
                if mask(hashlen[length](word).hexdigest()) == mask(line):
                    print word
#                    if line in rotX(hashlen[length](word).hexdigest(),i):
#                        print word, "(%d,%d)" % (w,i)
#                        done = True
