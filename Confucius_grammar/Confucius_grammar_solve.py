#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        line_output = []
        sentenances = line.split('.')
        for sentenance in sentenances:
            if len(sentenance)==0: continue
            sent_output = []
            words = [w for w in sentenance.split(' ') if len(w) != 0]
            sent_output.append(words[0].title())
            for word in words[1:]:
                if len(word)==0: continue
                if word.lower() == 'i':
                    sent_output.append("I")
                else:
                    sent_output.append(word.lstrip().strip().lower())
            line_output.append(' '.join(sent_output) + '.')
            
        print ' '.join(line_output)

