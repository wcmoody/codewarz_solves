#!/usr/bin/env python
import re
import requests
import bs4 
import sys

if len(sys.argv) != 2:
    exit("usage: need a url argument")

url = sys.argv[1]
headers = {}

results = []
r = requests.get(url)
results.append(r.headers['Etag'].replace('"',''))
headers['If-None-Match'] = r.headers['Etag']

while True:
    r = requests.get(url,headers=headers)
    headers['If-None-Match'] = r.headers['Etag']#','.join(h)
    h = r.headers['Etag'].replace('"','')
    if h not in results:
        results.append(h)
    else: break

from string import printable
from hashlib import sha1
myhashes = {}
for c in printable:
    h = sha1(c).hexdigest()
    myhashes[h] = c

flag = ''

for i in range(0,len(results),2):
    h = results[i] + results[i+1]
    flag += myhashes[h]

print flag






