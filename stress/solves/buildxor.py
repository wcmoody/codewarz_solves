import random

words = open('american-english.txt','r').read().split('\n')

def buildmessage(i):
    message = []
    for j in range(1000):
        thisword = words[random.randint(0,len(words))]
        message.append(thisword)
    return ' '.join(message)

def xor(msg,key):
    return ''.join([chr(ord(x) ^ key) for x in msg])

for i in range(8):
    with open("xor-%d.data" % i, 'w') as output:
        key = random.randint(0, 255)
        output.write(xor(buildmessage(i),key))

