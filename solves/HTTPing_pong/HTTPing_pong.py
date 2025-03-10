#!/usr/bin/env python

import requests
import re
import sys
from bs4 import BeautifulSoup as bs

usage = "usage: %s <url1> <url2> <starting_word>" % sys.argv[0]

if len(sys.argv) < 4:
    exit(usage)

patt= re.compile('(CWN\{[^\{}]*\})')
reply = re.compile("\w+ serving (\w*) to \w+")

i = 0

url1 = sys.argv[1]
url2 = sys.argv[2]
payload = sys.argv[3]

s = requests.session()
html = ""
params = {}

html = s.get(url1).text
field1 = bs(html,'html5lib').form.find_all('input')[0].get('name')

html = s.get(url2).text
field2 = bs(html,'html5lib').form.find_all('input')[0].get('name')

i = 0
while True:
    if i%2 == 0:
        html = s.post(url1,data={field1:payload}).text
        matches = patt.findall(html)
        if matches:
            print matches[0]
            break
        payload = reply.findall(html)[0]
    else:
        html = s.post(url2,data={field2:payload}).text
        matches = patt.findall(html)
        if matches:
            print matches[0]
            break
        payload = reply.findall(html)[0]
    i += 1


