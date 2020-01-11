#!/usr/bin/env python
import sys
import socket
import string
import re

patt= re.compile('(CWN\{[^\{}]*\})')

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

#get header
readuntil(mysock, 'Good luck!\n')

#get challenge
while True:
    prompt = readuntil(mysock, '\n')
    matches = patt.findall(prompt)
    if matches:
        print matches[0]
        break

    #get values
    payload = ""
    parts =  prompt.split('+')
    for part in parts:
        vals = part.strip().split(' ',1)
        payload += int(vals[0]) * vals[1]

    mysock.send(payload + "\n")
    response = readuntil(mysock,'\n')

mysock.close()


"""
Welcome to the repeater!
Simply follow the directions and you will get the flag!
Send the character the number of times indicated...
5 Q + 1 t
QQQQQt
Good luck!
56 Y + 48 p
"""


