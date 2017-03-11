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
        data = the_socket.recv(2)
        if not data: break
        total_data.append(data)
    return ''.join(total_data)

if len(sys.argv) != 3:
    exit(usage)

ip, port = sys.argv[1], int(sys.argv[2])
port = int(port)
answer = ''
for i in [str(i) for i in range(9932)]:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((ip,port))
    mysock.recv(1024)
    mysock.send("givechar " + i+'\n')
    response = recv_basic(mysock)
    if 'usage' not in response:
        answer += response[0]
        if response[0] == "}": break
    mysock.close()

print answer
