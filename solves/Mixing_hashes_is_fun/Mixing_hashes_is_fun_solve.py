#!/usr/bin/env python
import sys
from hashlib import sha1, sha256, sha224, sha512, md5, sha384

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

#words = "knowledge is a weapon arm yourself well before you ride forth to \
#battle".split(' ')

hs = {32: md5, 40:sha1, 56:sha224, 64:sha256, 96:sha384, 128:sha512}
revhs = {}
for k,v in hs.items():
    revhs[v] = k

def findhashes(h):
    lh = len(h)
    candidates = []
    if lh in hs.keys():
        candidates.append([hs[lh],])
    if 2*lh in hs.keys():
        candidates.append([hs[2*lh],])
    for hsk in hs.keys():
        halflen = hsk / 2
        if halflen < lh:
            if 2*(lh-halflen) in hs.keys():
                candidates.append([hs[hsk],hs[2*(lh-halflen)]])
    return candidates

def hashlookup(partialhash, hf, half):
    #print "looking for %s" % (partialhash)
    boom = False
    if partialhash == "a542e9b744bedcfd" and \
            hf.__name__.split('_')[-1] == 'md5':
        boom = True
    for word in words:
        hc = hf(word).hexdigest()
        if not half: hcl = len(hc)
        else: hcl = len(hc)/2
        #if boom:
        #    print hc
        #    print hc[:hcl]
        #    print hc[hcl:]
        if partialhash in (hc, hc[:hcl], hc[hcl:]):
            #print "found %s" % word
            return word
    return None
        

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    solution = []
    for line in lines:
        if len(line) == 0: continue
        for h in line.split(' '):
            #print len(h)
            cand = findhashes(h)
            for c in cand:
                lenhash1 = revhs[c[0]]
                if len(c) == 2:
                    #check for two half hashes combined
                    cw1 = h[:lenhash1/2]
                    cw2 = h[lenhash1/2:]
                    myword1 = hashlookup(cw1,c[0],True)
                    myword2 = hashlookup(cw2,c[1],True)
                    if myword1 != None:
                        solution.append(myword1)
                    if myword2 != None:
                        solution.append(myword2)
                    if myword2!= None or myword1!= None:
                        break

                if len(c) == 1:
                    #check for single full or half hash
                    myword = hashlookup(h,c[0],False)
                    if myword != None:
                        solution.append(myword)
                        break
                    myword = hashlookup(h,c[0],True)
                    if myword != None:
                        solution.append(myword)
                        break

                        

print ' '.join(solution)
                
            
