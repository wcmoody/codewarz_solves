#!/usr/bin/env python

import sys
import requests
import json
import re
import gzip
import operator

patt = re.compile('CWN{[^{}]*}')

usage = "usage: %s <geo_ip_service> <log_file.gz>" % sys.argv[0]

if len(sys.argv) < 3:
    exit(usage)

with gzip.GzipFile(sys.argv[2]) as f:
    data = f.read()

results = {}
s = requests.session()
url = sys.argv[1]

for line in data.split('\n'):
    if len(line) == 0: continue
    ip = line.split(' ')[0]
    r = s.get(url+'/json/'+ip)
    j = json.loads(r.text)
    country = j['country']
    if country not in results.keys():
        results[country] = 0
    results[country] += 1

abc_sort = sorted(results.items(), key=operator.itemgetter(0))
sorted_keys = sorted(abc_sort, key=operator.itemgetter(1),reverse=True)

for code, count in sorted_keys:
    print code, '*' * count
