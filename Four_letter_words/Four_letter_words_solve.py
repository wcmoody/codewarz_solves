#!/usr/bin/env python
import sys
import hashlib

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

hashes = {}
words = open('/usr/share/dict/american-english','r').readlines()
#words = open('american-english.txt','r').readlines()
for word in words:
	if len(word.strip()) == 4:
		hashes[hashlib.md5(word.strip()).hexdigest()] = word.strip()
		hashes[hashlib.sha1(word.strip()).hexdigest()] = word.strip()
		hashes[hashlib.sha224(word.strip()).hexdigest()] = word.strip()
		hashes[hashlib.sha256(word.strip()).hexdigest()] = word.strip()
		hashes[hashlib.sha384(word.strip()).hexdigest()] = word.strip()
		hashes[hashlib.sha512(word.strip()).hexdigest()] = word.strip()
#with open('allhashes.txt','w') as output:
#		for myhash,word in hashes.items():
#				output.write(word+'\t'+myhash+'\n')
				

#print len(hashes.keys())

with open(sys.argv[1],'r') as myinput:
		for line in myinput:
			if line.strip() in hashes.keys():
				print hashes[line.strip()]
    
