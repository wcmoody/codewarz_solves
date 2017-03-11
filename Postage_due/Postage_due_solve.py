#!/usr/bin/env python
import sys
import bs4

usage = "%s <url>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

import requests
import re

pattern = re.compile(r'<span class="math">(.*)</span>')


url = sys.argv[1]

def domath(op1, op2, operator):
    if operator in ("+", "plus"):
        return op1 + op2
    if operator in ('times', "multiplied by", "x"):
        return op1 * op2
    if operator in ("/", "divided by"):
        return op1 / op2
    if operator in ('-','minus'):
        return op1 - op2
    if operator == "subtracted from":
        return op2 - op1
    else: return "error %s" % operator

r = requests.get(url)
#print r.text
#throwaway = raw_input("pause...")

while True:
    soup = bs4.BeautifulSoup(r.text)
    inputs = [(element['name'],element['value']) for element \
            in soup.find_all('input') if element['type'] == 'hidden' ]
    inputs.append(("Send It!", "Send It!"))
    payload = {}
    for i, v in inputs:
        payload[i] = v
    expr = pattern.findall(r.text)[0]
    operand1 = int(expr.split(' ')[0])
    operand2 = int(expr.split(' ')[-1])
    operator = ' '.join(expr.split(' ')[1:-1]).decode('ascii')
    #print operand1, operand2, operator, 
    result = domath(operand1, operand2, operator)
    #print '=', result
    #print inputs
    payload['answer'] = result
    r = requests.post(url, data=payload)
    #print r.text
    if "nope" in r.text:
        print "*******Error**********"
        print r.text
    if "CTD{" in r.text:
        print r.text
        break

