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

if len(sys.argv) < 2:
    exit(usage)

ip, port = open(sys.argv[1],'r').read().split(' ',1)
port = int(port)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((ip,port))

letters = ''.join([chr(x) for x in range(0x41,0x41+26)])
letters = letters[::-1]

payload = "MADEYEMOODY"

def countones(string):
    val = int(string)
    mybin = bin(val)[2:]
    return mybin.count('1')

readuntil(mysock,"\n") #give me something to encode
mysock.send(payload+'\n')
result = readuntil(mysock,"\n").strip()

readuntil(mysock,"\n") # now decode this
challenge =  readuntil(mysock,'\n')
response = []
for word in challenge.split('||'):
    answer = ''
    for letter in word.split('.'):
        answer += letters[countones(letter)-1]
    response.append(answer)
    
final = ' '.join(response)
print final 
mysock.send(final+'\n')
readuntil(mysock,'...\n')
print readuntil(mysock,'}\n')

mysock.close()

