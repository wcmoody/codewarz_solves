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
        data = the_socket.recv(512)
        if not data: break
        total_data.append(data)
    return ''.join(total_data)

if len(sys.argv) != 3:
    exit(usage)

ip, port = sys.argv[1], int(sys.argv[2])
port = int(port)

moves = "ecsi"
attacks = {'ec':2 ,'ce':1, 'es':1, 'se':2, 'ic':1, 'ci':2, 'ei':2, 'ie':1,
        'cs':2 , 'sc':1, 'si':2, 'is':1}

flag = False

while not flag:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((ip,port))
    wins = 0
    while wins < 5:
        prompt = readuntil(mysock, 'Make yer Move\n')
        mysock.send('i\n')
        reply = readuntil(mysock, '!\n')
        reply += readuntil(mysock, '!\n')
        if "Congrats" in reply:
            wins +=1
            if wins == 5:
                flagmsg = readuntil(mysock,'}')
                flagmsg = readuntil(mysock,'}')
                print re.findall('CWN{.*}',flagmsg)[0]
                flag = True
        else:
            mysock.close()
            break



"""
with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        index = lines.index(line)
        rounds = line.split(' ')
        for i, rnd in enumerate(rounds):
            if rnd[0] not in moves and rnd[1] not in moves:
                print "Illegal moves by both players!"
                break
            if rnd[0] not in moves:
                print "Illegal move by Player 1!"
                break
            if rnd[1] not in moves:
                print "Illegal move by Player 2!"
                break
            if rnd in attacks.keys():
                print "Player %d Wins!"% attacks[rnd]
                break 
            if i == len(rounds)-1: 
                print "Draw!"
"""
            



