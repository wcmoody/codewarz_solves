#!/usr/bin/env python
import sys
import socket
import string
import random
from string import letters, digits, punctuation

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

while True:
    
    payload = "".join([random.choice(letters + digits + punctuation) for _ in \
        range(1024)])

    ip, port = sys.argv[1], int(sys.argv[2])
    port = int(port)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((ip,port))

    msg = readuntil(mysock,'>').strip()
    #print msg
    payload = raw_input('> ')
    print "Sending:", payload
    mysock.send(payload + '\n')
    print "Received:",recv_basic(mysock)




