#!/usr/bin/env python
import sys
import zlib
import socket
import string
import re
import time
from itertools import product
from Crypto.Cipher import XOR
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


#standby =r'Standby for your encrypted message\.\.\.\n' 
#accept = r'Do you accept this mission? \(y/n\)\n'

#patt= re.compile(standby + r'(.*)' + accept)

timepatt = '%Y-%m-%d %H:%M:%S'

ip, port = sys.argv[1], int(sys.argv[2])
port = int(port)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((ip,port))
opening = readuntil(mysock,'Do you accept this mission? (y/n)\n')
data = opening.split(chr(0x0a))
#print data[:4],
#for d in data[:4]:
#    k, v = d.split(':',1)
#    result[k.strip()] = v.strip()
message = opening.split('...')[1].split('Do')[0].strip().lstrip()
decomp =  zlib.decompress(message)
times = data[0].split("is: ")[1]
now = int(time.mktime(time.strptime(times, timepatt)))
bin_now = bin(now)
now = int(bin_now[2:])
answer = []
for word in decomp.split(','):
    decode = ''
    for letter in word.split('___'):
        x = int(letter)
        bits = str(x^now)
        if len(bits) == 30:
            bits = '0' + bits
        l = chr(int(bits[:7],2))
        decode += l
    answer.append(decode)
#print ' '.join(answer)
reply = ' '.join(answer)

mysock.send('y\n')
readuntil(mysock,'and I will give you a key!!!\n')
mysock.send(reply+'\n')
readuntil(mysock,'!\n')
print readuntil(mysock, '}').lstrip()
