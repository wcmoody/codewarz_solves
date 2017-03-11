#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

def test1(code,lin):
    reply = ''
    if len(code) > 79:
        reply = "yo man, this line is long (%d > 79 characters)" % len(code)
    return reply

def test2(code,lin):
    reply = ''
    if "import" in code[:6] and "," in code: # and "from" not in code:
        reply = "come on! keep these one to a line"
    return reply

def test3(code,lin):
    hashfound = False
    reply = ''
    for i in range(0,len(code)-1):
        if not hashfound:
            if "#" == code[i] and "# " != code[i:i+2]:
                reply = "shouldn't there be a hashtag AND a space?"
        if code[i] == '#': hashfound = True
    return reply

def test4(code,lin):
    hashfound = False
    reply = ''
    for i in range(1,len(code)-2):
        if not hashfound:
            if code[i] == '#' and code[i-2:i] != "  ":
                reply = "gimme gimme gimme 2 spaces for inline comment"
        if code[i] == '#': hashfound = True
    return reply

def test5(code,lin):
    reply = ''
    i = 0
    while code[i]==' ':
        i += 1
    if i % 4 != 0:
        reply = 'quad spaces FTW'
    return reply

def test6(code,lin):
    reply = ''
    if code[-1] == ' ':
        reply = "Trailing hEx 20 yo"
    return reply

def test7(code,lin):
    reply = ''
    if lin > 2 and code.lstrip()[:4] == 'def ':
        if lines[lin-1] != '' or lines[lin-2] != '':
            reply = "two yes! one no!"
    return reply

tests = [test1, test2, test3, test4, test5, test6, test7]

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for i, line in enumerate(lines):
        if line[:2] == "#!" and i==0: continue
        if len(line) == 0: continue
        for test in tests:
            response = test(line,i)
            if len(response) > 0:
                print "{}{:5d} {}".format(sys.argv[1], i+1, response)



