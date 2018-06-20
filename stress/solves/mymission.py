def myXor (key, cipher):
    output = ''
    for i in range(0,len(cipher),5):
        for c,k in zip(cipher[i:i+5],key):
            output += chr(ord(c) ^ ord(k))
    return output

cipher = open(pickAFile(),'r').read()
magic = open(pickAFile(),'r').read().split('\n')

cipher = cipher[:-1].decode('hex')
magic = [mag.decode('hex') for mag in magic]

keys = []
for number in magic:
  key = myXor(number, cipher[:len(number)])
  keys.append(key)

setMediaPath()

for i, key in enumerate(keys):
filename = 
  output = open(getMediaPath("%d-guess"%i),"w")
  output.write(myXor(cipher,key))
  output.close()  