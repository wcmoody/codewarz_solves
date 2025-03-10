#!/usr/bin/env python
import sys

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
        left, right = line.split('=',1)
        try:
            left = eval(left)
            right = eval(right)
            if left == right:
                print "True:   %s" % line
            else:
                print "False:  %s" % line
        except:
            print "Error:  %s" % line
