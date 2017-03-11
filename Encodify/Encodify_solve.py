#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


dictionaryfile = open('/usr/share/dict/american-english','rt')
#dictionaryfile = open('/tmp/american-english','rt')

words = [w for w in dictionaryfile.read().split('\n')]
#hexwords = [word.encode('hex') for word in words]

with open(sys.argv[1],'r') as myinput:
    lines = [line for line in myinput.read().split('\n')]
    for line in lines:
        if len(line) == 0: continue
        output = []
        for word in line.split(' '):
            if word.isdigit(): 
                #print "%s is digits" % word
                output.append(word); 
            elif len(word.split('.',1)) == 2:
                lefthalf, righthalf = word.split('.',1)
                if lefthalf.isdigit() and righthalf.isdigit():
                    output.append(word)

            elif len(word.split(',')) > 1:
                parts = word.split(',')
                if all(part.isdigit() for part in parts):
                    output.append(word)

            elif len(word)==1 and (word=="I" or word=="a"):
                #print "%s is a single letter word" % word
                output.append(word)
            elif word in words and len(word)!= 1:
                #print "%s is in dictionary" % word 
                output.append(word)
            elif word.lower() in words and len(word)!=1:
                output.append(word)
            elif word.encode('rot13').lower() in words:
                #print "%s is rot13 %s" % (word,word.decode('rot13'))
                output.append(word.decode('rot13'))
            elif len(word) % 4 == 0 or (word[-2:] == "==" or word[-1:]=="="):
                try:    
                    if word.decode('base64').lower() in words:
                        #print "%s is base64 %s" % (word,word.decode('base64'))
                        output.append(word.decode('base64'))
                except:
                    pass
                try:
                    #print "trying...",word, word.encode('rot13')
                    if word.encode('rot13').decode('base64').lower() in words:
                        #print "%s is rot13 and base64" % word.decode('rot13').decode('base64')
                        output.append(word.encode('rot13').decode('base64'))
                except:
                    pass

                try:
                    if word.decode('base64').encode('rot13').lower() in words:
                        #print "%s is base64 and rot13" % word.decode('base64').decode('rot13')
                        output.append(word.decode('base64').encode('rot13'))
                except:
                    pass

        print ' '.join(output)
