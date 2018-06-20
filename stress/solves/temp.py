# coding: utf-8
for word in cipher.split(' '):
    print word[:len(word)/2][::-1]; if len(word)%2==1: print word[len(word)/2]
    print word[int(round(len(word)/2.)):][::-1]
    
