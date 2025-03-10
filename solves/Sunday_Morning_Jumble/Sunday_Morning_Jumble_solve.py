#!/usr/bin/env python
import sys
import socket
import string
from itertools import permutations
from hashlib import sha1, sha256, sha224, sha512, md5, sha384

hashlen = {32:md5, 40:sha1, 64:sha256, 56:sha224, 96:sha384, 128:sha512}

try:
    with open('/usr/share/dict/american-english','r') as thedict:
        words = thedict.read().split('\n')
except:
    with open('./american-english','r') as thedict:
        words = thedict.read().split('\n')


def getwords(length):
    thelist = []
    for word in words:
        if len(word.split("'")[0]) == length:
            thelist.append(word.split("'")[0])
    return thelist


usage = "%s host port" % sys.argv[0]

def readuntil (s, mes):
    data = ""
    while not (mes in data):
        data += s.recv(1)
    return data


def recv_basic(the_socket):
    total_data=[]
    while True:
        data = the_socket.recv(8192)
        if not data: break
        total_data.append(data)
    return ''.join(total_data)

if len(sys.argv) != 3:
    exit(usage)

ip, port = sys.argv[1], int(sys.argv[2])
port = int(port)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((ip,port))

line1 = readuntil(mysock,"\n")
line2 = readuntil(mysock,"\n")
w = line2.split(' ')[1].strip('\n')
line3 = readuntil(mysock,"\n")
h = line3.split(' ')[1].strip('\n')
line4 = readuntil(mysock,"\n")
mysock.send("Y\n")
line5 = readuntil(mysock,"\n")
length = int(line5.split(' ')[6].replace('.','').strip('\n'))
line6 = readuntil(mysock,"\n")

hlen = len(h.strip())
phash = hashlen[hlen]

words_of_length = getwords(length)

for lw in words_of_length:
    
    if phash(lw).hexdigest() == h.strip():
        mysock.send(lw+'\n')
        reply = readuntil(mysock, '}')
        print reply
        break

