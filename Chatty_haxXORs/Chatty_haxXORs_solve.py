#!/usr/bin/env python
import sys
from scapy.all import *
import re


def value(ipaddr):
    binary = 0
    octets = ipaddr.split('.')
    for i,o in enumerate(octets):
        binary += int(o) << (8*(3-i))
    return binary

cipherpatt = re.compile(r'\[(\w+)\] \*\*\*SECRET\*\*\* ([0-9a-f]+)')
keypatt = re.compile(r'\[(\w+)\] \*\*\*KEY BROADCAST\*\*\* 0x([0-9a-f]{2})')

usage = "%s <input_file>" % sys.argv[0]

def myXOR(cipher,key):
    pt = ""
    for letter in cipher:
        pt += chr(ord(letter) ^ key)
    return pt


if len(sys.argv) < 2:
    exit(usage)

packets = rdpcap(sys.argv[1])
history = {}
records = {}
keys = {}
for i, packet in enumerate(packets):
    if Raw in packet:
        thismessage = packet[Raw].load
        match = keypatt.findall(thismessage)
        if match:
            user = match[0][0]
            key = int(match[0][1], 16)
            keys[user] = key
        match = cipherpatt.findall(thismessage)
        if match:
            user = match[0][0]
            plaintext = myXOR(match[0][1].decode('hex'),keys[user])
            if plaintext not in history.keys():
                print "%s ==> %s" % (user,plaintext), 
            history[plaintext] = packet[IP].dst


