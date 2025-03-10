#!/usr/bin/env python
import sys
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

"""
the five boxing wizards jump quickly
-|-/-/[- ]]=!v[- 13())(!^/gee VV!"/_@(r)[)$ ,|(_)[V][]D 0_(_)!<]{|_9

ylkciuq pmuj sdraziw gnixob evif eht
9|_]{<!(_)0_ []D[V](_),| $[)(r)@"/_!VV gee^/!)(()13 [-v!]]= [-/-/-|-

the ]]=!v[- gnixob $[)(r)@"/_!VV jump 0_(_)!<]{|_9

anotherbadword
@^/()-|-/-/[-(r)13@[)VV()(r)[)
drowdabrehtona
[)(r)()VV[)@13(r)[-/-/-|-()^/@

aaqqqq the ]]=!v[- gnixob abadwordz $[)(r)@"/_!VV jump 0_(_)!<]{|_9 yyyyyooo
[)(r)()VV[)@13(r)[-/-/-|-()^/@ the five boxing wizards jump quickly
-|-/-/[- ]]=!v[- 13())(!^/gee VV!"/_@(r)[)$ ,|(_)[V][]D 0_(_)!<]{|_9 yyyyyooo
"""

letters = {'-|-': 't', '/-/': 'h', '[-': 'e', ']]=': 'f', '!': 'i', 'v': 'v', '13': 'b', '()': 'o', ')(': 'x',
           '^/': 'n', 'gee': 'g', 'VV': 'w', '"/_': 'z', '@': 'a', '(r)': 'r', '[)': 'd', '$': 's', ',|': 'j',
           '(_)': 'u', '[V]': 'm', '[]D': 'p', '0_': 'q', '<': 'c', ']{': 'k', '|_': 'l', '9': 'y'}


def leet(string):
    answer = ''
    buff = ''
    for char in string:
        buff += char
        if buff in letters.keys():
            answer += letters[buff]
            buff = ''
    return answer

words = open('/usr/share/dict/american-english','r').readlines()
words = [w.strip() for w in words]

with open(sys.argv[1],'r') as myinput:
    lines = myinput.readlines()
    for line in lines:
        if len(line.strip()) == 0: continue
        tokens = line.strip().split()
        validoutput = False
        for token in tokens:
            english = leet(token)
            if english in words:
                print english,
                validoutput = True
            elif english[::-1] in words:
                print english[::-1],
                validoutput = True
            elif token in words:
                print token,
                validoutput = True
            elif token[::-1] in words:
                print token[::-1],
                validoutput = True
        if validoutput: print
