#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

wifi = {}
wifi = []

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    header = lines[0]
    fields = header.split(',')
    for line in lines[1:]:
        if len(line) == 0: continue
        newdict = {}
        #wifi[line] = {}
        data = line.split(',')
        if len(data) != len(fields):
            print "wrong length"
            break
        for i in range(len(fields)):
            newdict[fields[i]] = data[i]
        wifi.append(newdict)

def handletime(time):
    mydate, mytime = time.split(' ',1)
    month, day, year = mydate.split('/')
    hour, minute = mytime.split(':')
    yearminutes = int(year) * 12 * 31 * 24 * 60
    monthminutes = int(month) * 31 * 24 * 60
    dayminutes = int(day) * 24 * 60
    hourminutes = int(hour) * 60
    return int(minute) + hourminutes + dayminutes + monthminutes + yearminutes 

def flipdate(time):
    mydate, mytime = time.split(' ',1)
    month, day, year = mydate.split('/')
    hour, minute = mytime.split(':')
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    if len(hour) == 1:
        hour = '0' + hour
    mytime = ':'.join((hour,minute))
    return '/'.join((year,month,day)) + " " + mytime + ":00"

for v in wifi:
    if 'Type' in v.keys():
        if v['Type'] != 'wifi':
            wifi.pop(wifi.index(v))

for v in wifi:
    v['sort'] = handletime(v['FirstSeen']) 
    v['date'] = flipdate(v['FirstSeen'])

def printEntry(mydict):
    outputkeys = ['MAC','SSID','LAT','LON','date']
    outputvalues = [mydict[ok].lower() for ok in outputkeys]
    print ' '.join(outputvalues)

seenmac = []

wifi = sorted(wifi, key=lambda v: v['SSID'])
wifi = sorted(wifi, key = lambda v: v['sort'],reverse = True)
 
for s in wifi:
    if s['MAC'] not in seenmac:
        if "1969" not in s['date']:
            if s['Type'] == 'wifi':
                printEntry(s)
                seenmac.append(s['MAC'])






