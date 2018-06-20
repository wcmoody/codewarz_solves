import random

def rotbase(string):
    return string.encode('rot13').encode('base64').strip()

def baserot(string):
    return string.encode('base64').encode('rot13').strip()

def base(string):
    return string.encode('base64').strip()

def rot(string):
    return string.encode('rot13').strip()

def notouch(string):
    return string

"""
for word in ['clay','william','madeye','moody', 'clemson']:
    print word
    print rotbase(word)
    print baserot(word)
    print rot(word)
    print base(word)
"""

df = open('/tmp/american-english','rt')
words = df.read().split('\n')
df.close()

funct = {0:rotbase, 1:baserot, 2:base, 3:rot, 4:notouch}

output = open('./testcase.txt','wt')
for _ in range(100):
    controlstring = []
    encodestring = []
    for _ in range(5):
        index = random.randint(0,len(words)-1)
        print words[index]
        controlstring.append(words[index])
        encodestring.append(funct[index%5](words[index]))
    output.write(' '.join(controlstring)+"\n")
    output.write(' '.join(encodestring)+"\n")
output.close()



