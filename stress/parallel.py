import requests
import os
from bs4 import BeautifulSoup as bs
import thread
import time

url = 'https://2bn.codewarz.ninja/'
solves = os.listdir('solves')

def solveall(threadname,username,password):
    output = open('threads/'+threadname+'.log','a')
    output.write(str(time.time())+'\n')
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
    codes['Hello_World']='halloworld.py'
    for chall,solve in zip(challenges,solves):
        codes[chall.split('/')[2]] = solve 

    for challenge in challenges:
        challname = challenge.split('/')[2]
        if challname not in codes.keys(): continue
        output.write("Submitting for challenge: " + challname+'\n')
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
    output.close()

users = ['test_user'] * 3
passwords = ['goarmybeatnavy123!@#'] * 3

print users
print passwords


try:
    #thread.start_new_thread(solveall, ('one',))
    for u,p in zip(users,passwords):
        thread.start_new_thread(solveall, (u+p,u,p,))
except:
    print "Error: unable to start threads"

while 1:
    pass








