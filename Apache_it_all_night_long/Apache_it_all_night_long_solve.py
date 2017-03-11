#!/usr/bin/env python
import sys
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

pattern = re.compile(r'\"[^\"]+\"$')

useragent = {}
basefile = open(sys.argv[1],'rt')
filename = basefile.read().strip()
basefile.close()

with open(filename,'r') as myinput:
    for line in myinput:
        matches = pattern.findall(line.strip())
        if matches and matches[0] != '"-"':
            agent = matches[0]
            if agent not in useragent.keys():
                useragent[agent]=0
            useragent[agent] += 1
allagents = []
for agent,count in  useragent.items():
    allagents.append({'agent': agent ,'count':count})

allagents = sorted(allagents, key=lambda a: a['agent'])
allagents = sorted(allagents, key=lambda a: a['count'])

bins = 50
maxstars = max([a['count'] for a in allagents])
fmat = "{:>%ss}" % int(round(maxstars/bins+1))
for agent in allagents:
    numstars = int(round(agent['count']/bins+1))
    output = fmat.format('*' * numstars)
    output += ": {} {}".format(agent['count'],agent['agent'])
    print output
