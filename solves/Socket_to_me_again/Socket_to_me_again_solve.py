#!/usr/bin/env python
import sys
import socket
import string
import time

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
readuntil(mysock, 'What do you want?\n').strip()
mysock.send('getkey\n')
key = readuntil(mysock, '\n').strip().split(': ')[1]
mysock.close()
answer ={} 
for char in string.digits + string.punctuation + string.letters:
    time.sleep(2)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((ip,port))
    readuntil(mysock, 'What do you want?\n')
    mysock.send('givechar %s %s\n' % (char,key))
    reply = recv_basic(mysock).strip()
    if "such sad" not in reply:
        for i in reply.split(','):
            try:
                answer[int(i.strip())] = char
            except:
                print char, reply
    mysock.close()

print ''.join([answer[k] for k in sorted(answer.keys())])


