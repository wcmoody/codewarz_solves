#!/usr/bin/env python
import sys
import socket
import re
import string
from itertools import product

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

"""
)Welcome to the MafsBeHaaaaa)rd Service I will send "you )a
collection of numbers on )one line with a single numb)er on the next line. Send
m)e the math operators in the) appropriate order that wil)l make the collection
of nu)mbers equal the single numb)er (separate them with a ;)).(Our timer seems
to be bro)ken so work fast...)

200 7 18 256 228 138 248 122 76
1163.96
"""

prompt = readuntil(mysock, "fast...)\n").replace(')','')
charpat = re.compile('separate them with a (.)')
match = charpat.findall(prompt)
if match:
    joiner = match[0]

numbers = ['float(%s)'%x  for x in readuntil(mysock,'\n').strip('\n').split(' ')]
result_str = readuntil(mysock,'\n').strip('\n')
result = float(result_str)
precision = len(result_str.split('.')[-1])

operations = ['+', '-', '*', '/']
opcount = len(numbers) - 1

for ops in product(operations,repeat = opcount):
    mafs = [a for b in zip(numbers, ops) for a in b]
    mafs.append(numbers[-1])
    answer = eval(' '.join(mafs))
    if round(answer,precision) == result:
        flag = joiner.join(ops)
        mysock.send(flag+'\n')
        break

readuntil(mysock,'\n').strip()
flag = readuntil(mysock,'\n').strip()

print flag


mysock.close()

