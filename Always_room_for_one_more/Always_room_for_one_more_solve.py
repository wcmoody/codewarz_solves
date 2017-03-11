#!/usr/bin/env python
import sys
import re
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

patt = re.compile(r'add 1 to me: (-?\d+)')

ip, port = sys.argv[1], int(sys.argv[2])
port = int(port)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((ip,port))
output = mysock.recv(1024)
newlines = readuntil(mysock, "0a0a".decode('hex'))
#print output, output.encode('hex')
while True:
    value = int(patt.findall(output)[0])
    #print "sending %d" % (value+1)
    mysock.send(str(value+1)+'\n')
    output = mysock.recv(1024)
    if "{" in output:
        print output.split(': ')[1]
        break
    newlines = readuntil(mysock, "0a0a".decode('hex'))
    #print "output:", output, output.encode('hex')







