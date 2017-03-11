#!/usr/bin/env python
import time
import sys
import socket
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

pattern = re.compile(r'(\w+) (\d+) (and|by|from) (\d+)!')

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
				ip, port = line.strip().split(' ')
				port = int(port)
				mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				mysock.connect((ip,port))
				done = False
				readuntil(mysock, "ohaithar, Mr. User.\n")
				data = readuntil(mysock, "!\n")
				while (not done):
						matches = pattern.findall(data)
						for match in matches:
								if match[0] == 'add':
										ans = str(int(match[1]) + int(match[3]))
								if match[0] == 'subtract':
										ans = str(int(match[3]) - int(match[1]))
								if match[0] == 'multiply':
										ans = str(int(match[1]) * int(match[3]))
								if match[0] == 'divide':
										ans = "{:10.8f}".format(int(match[1]) / float(match[3]))
#								print "Answer is:", ans
								mysock.send(ans+'\n')
								time.sleep(1)
						dump = readuntil(mysock,"Great, here's one of my favorite tunes for you to enjoy!")
						dump = mysock.recv(8192)
						if "{" in dump: done = True
						else: data = dump[-1024:]
						
				print "CTD{"+dump.split('{')[-1]
				mysock.close()
#				print "Closed socket"
						
				



