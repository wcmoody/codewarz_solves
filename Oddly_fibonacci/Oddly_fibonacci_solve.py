#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

try:
    words = open('/usr/share/dict/american-english','r').read().split('\n')
except:
    words = open('./american-english.txt','r').read().split('\n')

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        num1, num2 = [int(x) for x in line.split(' ',1)]
        print sum([fib(n) for n in range(num1,num2) if fib(n)%2==1])


