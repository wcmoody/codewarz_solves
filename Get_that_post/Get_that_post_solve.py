#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup as bs
from re import compile

usage = "%s <input_file>" % sys.argv[0]

patt = compile('window.location.href = "(/\w*)";')

flagpatt = compile('RCN{[^}]*}')

s = requests.session()

if len(sys.argv) < 2:
    exit(usage)

url = sys.argv[1]
r = s.get(url)

soup = bs(r.text,features="html.parser")
brs = soup.find_all('br')
question = brs[1].nextSibling
action = soup.find_all('form')[0].get('action')
method =  soup.find_all('form')[0].get('method')

op1, decider, op2 = [w.strip('?') for w in question.split(' ')[-3:]]

if decider == 'from':
    result = int(op2) - int(op1)
elif decider == 'and':
    result = int(op2) + int(op1)

if method == "POST":
    headers = {'Referer':'http://gtp.runcode.ninja/'}
    aurl = url + action
    payload = {'answer':str(result)}
    r = s.post(aurl,data=payload,headers=headers)
    match = patt.findall(r.text)
    if match:
        rurl = url + match[0]
        done = False
        while not done:
            r = s.get(rurl,headers=headers)
            match2 = flagpatt.findall(r.text)
            if match2:
                done = True

print match2[0]
                

