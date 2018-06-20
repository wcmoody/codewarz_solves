import requests
import os
import time
from bs4 import BeautifulSoup as bs

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://codewarz.ninja/'

solves = os.listdir('solves')

s = requests.Session()

username = "redacted"
password = "redacted"

r = s.get(url, verify=False)
cookies = r.cookies
r = s.get(url+'login', cookies=cookies)
soup = bs(r.text, "html5lib")
inputs = [(element['name'],element['value']) for element \
        in soup.find_all("input", type="hidden") ]

payload = {}
for i,v in inputs:
    payload[i] = v

payload['username'] = username
payload['password'] = password
h = {"Referer":"https://codewarz.ninja/login", 
        "Content-Type": "application/x-www-form-urlencoded"}

r = s.post(url+'/login', headers = h, data=payload, cookies=cookies, verify=False)
r = s.get(url+'challenges', verify=False)


soup = bs(r.text,"html5lib")
challenges = []
for a in soup.find_all('a', href=True):
    if "do_challenge" in a['href']:
        challenges.append(a['href'])
for challenge in challenges:
    print challenge.split('/')[2]


# the block below has not been confirmed on current version
# this is because, well i don't have any challenges to submit solve for
"""
for challenge in challenges:
    challname = challenge.split('/')[2] + '.py'
    filename = challname
    print "Submitting for challenge:", challname
    r = s.get(url+challenge)
    challsoup = bs(r.text)
    inputs = [(element['name'],element['value']) for element \
            in challsoup.find_all('input') if element['type'] == 'hidden' ]
    payload = {}
    payload['submit'] = 'submit'
    for i, v in inputs:
        payload[i] = v
    src = [('code',(filename, open('solves/'+filename,'r'),'text/x-script.python'))]
    s.headers.update({'referer':'https://codewarz.ninja/challenges'}) 
    r = s.post(url+challenge,data=payload,files=src)
    print r.status_code
"""







#with open('test.html','w') as output:
#    output.write(r.text)



