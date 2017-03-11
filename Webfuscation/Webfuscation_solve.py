#!/usr/bin/env python
import requests
import bs4
from zlib import decompress as decomp
import json
import datetime
import sys

if len(sys.argv) < 2:
    exit("you need to provide the URL, duuuude!")

url = sys.argv[1]


def getletter(c):
    s = c['secure-session']
    return chr(int(decomp(decomp(s.decode('hex')))) >> 75)

s = requests.Session()

flag = '*' * 50

def replace(c,i):
    return flag[:i] + c + flag[i+1:]

while '*' in flag.split('}')[0]:
    r = s.get(url)
    epoch = int(r.cookies['mostest-securest-session'])
    char = getletter(r.cookies)
    window = int(r.headers['Date'])
    index = epoch - window
    flag = replace(char,index)

print flag.strip('*')


