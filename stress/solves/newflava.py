#!/usr/bin/env python
import sys
import re

pattern = re.compile(r'(\d+) (after|til) (\d+)')

if len(sys.argv) < 2:
    exit("usage: %s <input_file>" % sys.argv[0])

#angles = {}
#for a in range(0,360 + 1):
#    angles[a] = []

times = {}

def maketime(i):
    hours = i / 3600 % 12
    if hours == 0:
        hours = 12
    minutes = i % 3600 / 60
    seconds = i % 3600 % 60
    return (hours, minutes, seconds)

for i in range(0,43200+1):
    hours, minutes, seconds = maketime(i)
    hourmove = 360 - (hours * 30. + minutes * (30/60.) + seconds * (30/3600.))
    hourmove = hourmove % 360
    minutemove = minutes * 360/60. + seconds * (360/3600.)
    minutemove = minutemove % 360
    angle = (hourmove + minutemove) % 360
    times["{}:{:02d}:{:02d}".format(hours,minutes,seconds)] = \
        round(angle,1)%360 #add int() round to 1 digit

"""
with open('alltimes.txt', 'w') as output:
    sk = sorted(times.keys())
    for k in sk:
        output.write("%s: %f\n" % (k, times[k]))
#"""

def getnexthour(hour):
    if hour== 12:
        return 1
    else: return hour+1


def get2nexthour(hour):
    if hour== 12:
        return 2
    elif hour == 11:
        return 1
    else: return hour+1

def getprevhour(hour):
    ans = -1
    if hour == 1:
        ans = 12
    else: ans = hour-1
    return ans


def get2prevhour(hour):
    if hour == 1:
        ans =  11
    elif hour == 2:
        ans = 12
    else: ans = hour-2
    return ans

def get3prevhour(hour):
    if hour == 1:
        ans =  10
    elif hour == 2:
        ans =  11
    elif hour == 3:
        ans =  12
    else: ans =  hour-3
    return ans


def get4prevhour(hour):
    if hour == 1:
        ans =  9 
    elif hour == 2:
        ans =  10
    elif hour == 3:
        ans =  11
    elif hour == 4:
        ans =  12
    else: ans =  hour-4
    return ans

def nothour(h,d):
    return not((360 - (h % 12) * 30) % 360  == d)


with open(sys.argv[1]) as myinput:
    for line in myinput.read().split('\n'):
        if len(line) == 0: continue
        matches = pattern.findall(line)
        if not matches: continue
        degrees, direction, hour = matches[0]
        degrees = int(degrees)
        hour = int(hour)
        angle = (12-hour) * 30
        if direction == 'after':
            results = [t for t in times.keys() if times[t] == int(degrees)%360 and t.split(':')[0] == str(hour) and nothour(hour,degrees)]
            if len(results)==0: 
                results = [t for t in times.keys() if times[t] == int(degrees)%360 and t.split(':')[0] == str(getnexthour(hour))]
            if len(results)==0: 
                results = [t for t in times.keys() if times[t] == int(degrees)%360 and t.split(':')[0] == str(get2nexthour(hour))]
            try:
                print sorted(results,reverse=False)[0]
            except:
                print "after error", matches
            
        if direction == 'til':
            results = [t for t in times.keys() if times[t] == (degrees)%360 and t.split(':')[0] == str(getprevhour(hour))] 
            if len(results)==0:
                results = [t for t in times.keys() if times[t] == int (degrees)%360 and t.split(':')[0] == str(get2prevhour(hour))]
            if len(results)==0:
                results = [t for t in times.keys() if times[t] == int(degrees)%360 and t.split(':')[0] == str(get3prevhour(hour))]
            if len(results)==0:
                results = [t for t in times.keys() if times[t] == int(degrees)%360 and t.split(':')[0] == str(get4prevhour(hour))]
            try:
                print sorted(results,reverse=False)[0]
            except:
                print "til error", matches

"""
sortedkeys = sorted([k for k in times.keys()])
for k in sortedkeys:
    print k, times[k]
"""
