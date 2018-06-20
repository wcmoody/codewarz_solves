# coding: utf-8
words = open('/usr/share/dict/american-english.txt','r').readlines()
len(words)
for word in words:
    if len(word)==4: print word
    
