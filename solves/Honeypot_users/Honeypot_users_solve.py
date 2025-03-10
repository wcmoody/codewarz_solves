#!/usr/bin/env python
from operator import itemgetter
import os
import sys
import re

data = []

for filename in os.listdir(os.getcwd() + '/' + sys.argv[1]):
    with open(os.getcwd() + '/' + sys.argv[1] + '/' + filename) as f:
        data += f.readlines()

usermessage = """User account "%s" has been attempted "%s" times overall."""
passmessage = """    Password "%s" was attempted %s times."""

p = """login attempt \[(.*?)/(.*?)\]"""
patt = re.compile(p)
matches = patt.findall('\n'.join(data))

attempts = {}

for u,p in matches:
    if u not in attempts.keys():
        attempts[u] = {}
    if p not in attempts[u].keys():
        attempts[u][p] = 0
    attempts[u][p] += 1

#flatten info:
phase0 = {}
for user, passwords in attempts.items():
    pwds = [(p,n) for p,n in passwords.items()]
    phase0[user] = pwds

def dumpphase(phase):
    for u,p in phase.items():
        print "[+]", u
        for pp,n in p:
            print "\t[-]",pp,n

# sort each users password attempts alphabetically
phase1 = {}
for user, passwords in phase0.items():
    sort_by_alpha = sorted(passwords, key=itemgetter(0))
    phase1[user] = sort_by_alpha

# sort each users password attempts by count
phase2 = {}
for user, passwords in phase1.items():
    sort_by_count = sorted(passwords, key=itemgetter(1))
    phase2[user]  = sort_by_count 

#dumpphase(phase2)


def gettotal(tries):
    total = 0
    for p,n in tries:
        total += n
    return total


# sort all users by the first password in their list
all_users = []
for user, passwords in phase2.items():
    firstcount = int(passwords[0][1])
    firstpass = passwords[0][0]
    totattempts = gettotal(passwords)
    all_users.append((user,firstcount,firstpass,totattempts))

all_users = sorted(all_users, key=itemgetter(2))
all_users = sorted(all_users, key=itemgetter(1))
all_users = sorted(all_users, key=itemgetter(3))


#for e in all_users:
#    print e
#exit()

# sort by number of attempts of user (small to big)

for u,fc,fp,t in all_users:
    print usermessage % (u,t)
    for password in phase2[u]:
        print passmessage % password
