#!/usr/bin/env python
import sys
import re
import socket
import string
import random

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
    
def getrs(c, n):
    return ''.join(random.choice(c) for _ in range(n))

def part1(payload, cipher):
    mysock.send(payload+'\n')
    work = readuntil(mysock,'\n').strip()
    #print "[+] P1 - sent: %s" % payload
    #print "[+] P1 - received: %s" % work
    mapping = {}
    if len(work) == len(payload):
        for c,p in zip(work,payload):
            mapping[c] = p
    #print "[+] Mapping is:", mapping
    return ''.join([mapping[c] for c in cipher])    

def part2(control, goal):
    payload = ''.join(2*c for c in control)
    mysock.send(payload + '\n')
    work = readuntil(mysock,'\n').strip()
    #print "[+] P2 - sent %s" % payload
    #print "[+] P2 - recieved %s" % work
    for i in range(len(payload)):
        if work[i:] + work[:i] == payload:
            break
    
    #print "[+] Pivot point found as %d" % i
    return goal[i:] + goal[:i]    


def interactive(control, goal):
    while True:
        answer = raw_input('>>> ')
        mysock.send(answer + '\n')
        reply = readuntil(mysock,'\n').strip()
        #print reply
        #give = readuntil(mysock,'\n').strip()
        ##print give
        prompt = readuntil(mysock,'\n').strip()
        #print prompt

"""
[+] goal is: 0a8f665749bc8245082885ec136cf98e
>>> aabbccddeeff00112233445566778899
bcef124578abde0134679acdf0235689
Guess 7/9 (Round 4/4)
>>> 00112233445566778899aabbccddeeff
124578abde0134679acdf0235689bcef
Guess 8/9 (Round 4/4)

for r,d in zip(r1,conversion):
    guess += alpha[(alpha.index(r)+d) % 16]
    
for s,d in zip(s1,conversion):
    guess += alpha[(alpha.index(s)+d) % 16]
    
for s,d in zip(s1,conversion):
    guess += alpha[(alpha.index(s)+d) % 16]
    
guess = ''
for s,d in zip(s1,conversion):
    guess += alpha[(alpha.index(s)+d) % 16]
"""

def part4 (control, goal):
    payload = getrs(control, len(goal))
    mysock.send(payload + '\n')
    work = readuntil(mysock,'\n').strip()
    #print "[+] P4: - sent %s" % payload
    #print "[+] P4: - recieved %s" % work
    mymap = []
    for p,w, in zip(payload,work):
        d = control.index(w) - control.index(p)
        mymap.append(d)
    #print "[+] Mymap:", mymap
    payload = ''
    for g,d in zip(goal,mymap):
        payload += control[(control.index(g) - d) % len(control)]
    #print payload
    return payload



funcs = {1: part1, 2: part2, 3: part1, 4: part4}


welcome = readuntil(mysock,'\n').strip()
#print welcome
we = readuntil(mysock,'\n').strip()
#print we
your = readuntil(mysock,'\n').strip()
#print your
p1 = re.compile("Your character set is '(\w*)', max len is (\d+) characters.")
charset, length = p1.findall(your)[0]
#print "[+] character set:", charset
#print "[+] length is:", length

i = 1

while True:
    #print "========= WELCOME TO ROUND %d ========" % i
    give = readuntil(mysock,'\n').strip()
    #print give
    prompt = readuntil(mysock,'\n').strip()
    #print prompt

    p2 = re.compile("Give me a string that encrypts to '(\w*)'")
    goal = p2.findall(give)[0]
    #print "[+] goal is:", goal

    answer = funcs[i](charset, goal)
    #print "[+] Sending answer of:", answer
    
    prompt = readuntil(mysock,'\n').strip()
    mysock.send(answer+'\n')
    result = readuntil(mysock,'\n')
    #if goal.strip() == result.strip():
        #print "[+] Should see 'You got it!'"
    reply = readuntil(mysock,'\n').strip()
    #print "[+] Response:", reply
    if "You got it" in reply:
        i += 1
    #else:
        #print "[-] Trying again...."
    #s = raw_input("....press enter to advance....")
    if i==5:
        break

print mysock.recv(1024)


mysock.close()



