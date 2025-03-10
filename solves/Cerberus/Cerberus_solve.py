#!/usr/bin/env python
from hashlib import sha1
import itertools
import sys
import socket
import string
import re
import random

usage = "%s host port" % sys.argv[0]

def readuntil (s, mes):
    data = ""
    while not (mes in data):
        data += s.recv(1)
    return data


def recv_basic(the_socket):
    total_data=[]
    while True:
        data = the_socket.recv(2)
        if not data: break
        total_data.append(data)
    return ''.join(total_data)

if len(sys.argv) != 3:
    exit(usage)

host = sys.argv[1]
port = int(sys.argv[2])

prompt="""Give me a string starting with (\w+), of length (\d+), such that its sha1 sum ends in (\w+)."""

doworkpat = re.compile(prompt)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host,port))
readuntil(mysock,'\n')
question = readuntil(mysock,'\n')
#print question
#question += readuntil(mysock,'.')
start, length, end = doworkpat.findall(question)[0]
#print "s,l,e", start, length, end
length = int(length)
myprintable = string.digits + string.letters
target = length - len(start)
for ch in itertools.product(myprintable, repeat=target):
    #c = ''.join(random.choice(myprintable) for x in range(length-len(start)))
    c = ''.join(ch)
    #print "trying c: {}".format(c)
    if sha1(start+c).hexdigest()[-1*len(end):] == end:
        #print "Found string: {}".format(start+c)
        break
mysock.send(start+c+'\n')
print readuntil(mysock,'\n')

