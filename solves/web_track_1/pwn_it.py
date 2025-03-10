#!/usr/bin/env python
import requests
import re
from bs4 import BeautifulSoup as bs

patt = re.compile('RCN{[^}]*}')

s = requests.session()

url = "http://web-track-1.runcode.ninja/"

r = s.get(url)

soup = bs(r.text,features="html.parser")
links = [a['href'] for a in soup.findAll('a')]

enums = []
for link in links:
    if '/' in link[1:]:
        base = '/'.join(link.split('/')[:-1])
        enums.append(int(link.split('/')[-1]))


target = url + base + '/' + str(max(enums)+1)
r = s.get(target)

match = patt.findall(r.text)
if match:
    print match[0]


