#!/usr/bin/env python
import sys
import string
from bs4 import BeautifulSoup as bs
import requests
import re

usage = "%s <scrape url> <brute url>" % sys.argv[0]
pattern = re.compile(r'CTD\{.*\}')

if len(sys.argv) < 2:
    exit(usage)

base = sys.argv[1]

agent='flag'
payload = {'User-agent':agent}

r = requests.get(base, headers=payload)
soup = bs(r.text)
urls = [link.get('href') for link in soup.find_all('a')]
visited = []
while len(urls) > 0:
    url = urls.pop()
    r = requests.get(base + url, headers=payload)
    soup = bs(r.text)
    for newurl in [link.get('href') for link in soup.find_all('a')]:
        if newurl not in visited:
            urls.append(newurl)
    if "CTD{" in r.headers['X-secrets']:
        print pattern.findall(r.headers['X-secrets'])[0]
        exit()
    visited.append(url)
