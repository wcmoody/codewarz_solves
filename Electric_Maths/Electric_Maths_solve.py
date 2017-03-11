#!/usr/bin/env python
import time
import sys
import socket
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

pattern = re.compile(r'(\w+) (\d+) (and|by|from) (\d+)!')


with open(sys.argv[1],'r') as myinput:
		for line in myinput:
				ip, port = line.strip().split(' ')
				port = int(port)
				mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				mysock.connect((ip,port))
				data = mysock.recv(1024)
#				print "Data:",data
				maths = data.split('\n')[-1]
#				print "%d Maths:"%len(maths) ,maths
				matches = pattern.findall(maths)
				for match in matches:
#						print "0",match[0]
#						print "1",match[1]
#						print "3",match[3]
						if match[0] == 'add':
								ans = str(int(match[1]) + int(match[3]))
						if match[0] == 'subtract':
								ans = str(int(match[3]) - int(match[1]))
						if match[0] == 'multiply':
								ans = str(int(match[1]) * int(match[3]))
						if match[0] == 'divide':
								ans = "{:10.8f}".format(int(match[1]) / float(match[3]))
#						print "Answer is:", ans
						mysock.send(ans+'\n')
						time.sleep(1)
						print mysock.recv(1024)

				mysock.close()
#				print "Closed socket"
						
				



