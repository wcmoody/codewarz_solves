#!/usr/bin/env python
import sys
import requests

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

url = sys.argv[1]

print requests.get(url).text
