import requests
import os
import time
from bs4 import BeautifulSoup as bs

url = 'https://2bn.codewarz.ninja/'

solves = os.listdir('solves')


for i in range(5):
    s = requests.Session()
    user = 'test_user'
    password = 'goarmybeatnavy123!@#'

    r = s.get(url)
    cookies = r.cookies
    r = s.get(url+'login')
    soup = bs(r.text)
    inputs = [(element['name'],element['value']) for element \
            in soup.find_all('input') if element['type'] == 'hidden' ]
    payload = {}

    for i,v in inputs:
        payload[i] = v

    payload['username'] = user
    payload['password'] = password

    r = s.post(url+'login',data=payload,cookies=cookies)
    r = s.get(url+'challenges')

    soup = bs(r.text)
    challenges = []
    for a in soup.find_all('a', href=True):
        if "do_challenge" in a['href']:
            challenges.append(a['href'])

    codes = {}
    
    for chall,solve in zip(challenges,solves):
        codes[chall.split('/')[2]] = solve

    for challenge in challenges:
        challname = challenge.split('/')[2]
        if challname not in codes.keys(): continue
        print "Submitting for challenge:", challname
        r = s.get(url+challenge)
        challsoup = bs(r.text)
        inputs = [(element['name'],element['value']) for element \
                in challsoup.find_all('input') if element['type'] == 'hidden' ]
        payload = {}
        for i, v in inputs:
            payload[i] = v
        filename = codes[challname]
        src = [('user_code',(filename, open('solves/'+filename,'r'),'text/x-script.python'))]
        s.headers.update({'referer':'https://2bn.codewarz.ninja/challenges'}) 
        r = s.post(url+challenge,data=payload,files=src)








#with open('test.html','w') as output:
#    output.write(r.text)



