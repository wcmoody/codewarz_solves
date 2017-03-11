#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

known = """Over and over again
I relive the moment
I am bearing the burden within
Open wounds hidden under my skin

Pain is real as a cut that bleeds
The face I see every time I try to sleep
Staring at me crying"""

def jj(word):
    if len(word) == 3:
        return ''.join(word[i] for i in [1,0,2])
    if len(word) == 5:
        return ''.join(word[i] for i in [3,4,2,0,1])
    if len(word) == 7:
        return ''.join(word[i] for i in [2,3,5,6,4,0,1])
    if len(word) % 2 == 0:
        return ''.join([(word[i+1]+word[i]) for i in range(0,len(word),2)]) 
    else:
        return word

with open(sys.argv[1],'r') as myinput:
    solution = []
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: 
            solution.append('') 
            continue
        words = line.split(' ')
        solution.append(' '.join([jj(w) for w in (words[1:]+[words[0],])]))
        #index = lines.index(line)
        #print "[+] known:", known.split('\n')[index]
    if solution[-1] == '': solution=solution[:-1]
    print '\n'.join(solution)


