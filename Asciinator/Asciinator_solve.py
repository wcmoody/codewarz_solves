#!/usr/bin/env python
import sys
import socket
import string
from hashlib import md5

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

mychars = " " + string.uppercase


ip, port = sys.argv[1], int(sys.argv[2])
port = int(port)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((ip,port))

welcome = "normal letters back.\n"

readuntil(mysock, welcome)

mysock.send(mychars+'\n')

response = []

for i in range(8):
    response.append(readuntil(mysock,'\n').replace('\n',' '))

asciis = {}

msglen = len(response[0])
#print "message length is", msglen

for i, letter in enumerate(mychars):
    msg = ''
    for row in range(8):
        msg += response[row][9*i:9*i+9]
    asciis[md5(msg).hexdigest()] = letter

#for ascii_hash, letter in asciis.items():
#    print letter, ascii_hash

challenge = []
for i in range(8):
    challenge.append(readuntil(mysock,'\n').replace('\n',' '))

phrase = ''
for i in range(len(challenge[0])):
    msg = ''
    for row in range(8):
        m = challenge[row][9*i:9*i+9]
        msg += m
    h = md5(msg).hexdigest()
    if h in asciis.keys():
        phrase += asciis[md5(msg).hexdigest()]

#print phrase

readuntil(mysock,'letters...\n')
mysock.send(phrase + '\n')

readuntil(mysock,'\n') #Thank you message
print readuntil(mysock,'\n').strip() #flag




mysock.close()



