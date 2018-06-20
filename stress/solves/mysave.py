# coding: utf-8
data = open('last_friday_night_data1.txt', 'r').read()
counts = dict()
for i in items:
      counts[i] = counts.get(i, 0) + 1
    
for i in data:
      counts[i] = counts.get(i, 0) + 1
    
print counts
import operator
max(counts.iteritems(), key=operator.itemgetter(1)[0])
max(counts.iteritems(), key=operator.itemgetter(1))[0])
max(counts.iteritems(), key=operator.itemgetter(1))[0]
key = 0x11 ^ 0x20
print key
print "".join([chr(ord(x)^key) for x in data])
