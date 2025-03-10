#!/usr/bin/env python
import sys
import socket
import string

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


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


with open(sys.argv[1],'r') as myinput:
    for line in myinput:
        mapping = {}
        ip, port = line.strip().split(' ')
        port = int(port)
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((ip,port))
        data = readuntil(mysock, "What would you like me to encode?\n")
        payload = string.lowercase + string.uppercase + string.digits
        payload += "?.!{}[_@#$%^&*]" # string.punctuation + " \t"
        payload = '%s ' % payload * 150
        mysock.send(payload+"\n")
        readuntil(mysock, "Here you go!\n")
        encoded = readuntil(mysock, "\n")
        for w,ee in zip(payload.split(' '),encoded.split('||')):
            for l,e in zip(w,ee.split('.')):
                if e == '\n': continue
                if l not in mapping.keys():
                    mapping[l] = []
                if e not in mapping[l]:
                    mapping[l].append(e)
        #for k,v in mapping.items():
        #    print k, v
        #theAs = sorted([int(a) for a in mapping['A']])
        #for theA in theAs:
        #    print theA / float(min(theAs))
        nextprompt = "If you can decode this phrase, "
        nextprompt += "I will give you a flag!!!!\n"
        readuntil(mysock, nextprompt)
        flag = readuntil(mysock,'\n')
        flagwords = flag.split("||")
        final = []
        for word in flagwords:
            word = word.strip()
            answer = []
            for char in word.split('.'):
                answer.append((item for item in mapping.keys() if char in
                    mapping[item]).next())
            final.append(''.join(answer))

        mysock.send(' '.join(final)+'\n')
        solution = readuntil(mysock,"Thank you, come again!\n")
        print [line for line in solution.split('\n') if "{" in line][0]
        mysock.close()


