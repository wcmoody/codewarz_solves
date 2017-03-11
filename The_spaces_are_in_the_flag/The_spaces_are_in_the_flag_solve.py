#!/usr/bin/env python
import string
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

letters = \
"_cdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza"
#myinput = "18060717.0717!.25.18031718?.171816071205!"

with open(sys.argv[1],'r') as myinput:
    lines = myinput.readlines()
    for line in lines:
        myoutput = []
        if len(line.strip()) == 0: continue
        words = line.strip().split('.')
        for word in words:
            word = word.replace(" ",".")
            m = ''
            i = 0
            while i < len(word):
                if word[i] in string.punctuation:
                    m += word[i]
                    i += 1
                else:
                    m += letters[int(word[i:i+2])]
                    i += 2
                #try:
                #    index = int(word[i:i+2])
                #    if abs(index)!= index: raise ValueError("negatives...boo")
                #    m += letters[(int(word[i:i+2]))]
                #    i += 2
                #except:
                #    m += word[i]
                #    i += 1
            myoutput.append(m)
        print ' '.join(myoutput)
