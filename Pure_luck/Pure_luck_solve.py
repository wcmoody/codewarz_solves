#!/usr/bin/env python
import sys
import socket
import string

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
response = readuntil(mysock,'Pick a number from 0-25')
i = 0
while "{" not in response:
    mysock.send(str(i)+'\n')
    response = readuntil(mysock,'\n')
    i += 1
print response.strip()


