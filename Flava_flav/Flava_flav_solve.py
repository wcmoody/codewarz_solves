#!/usr/bin/env python
import sys
import re

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

pattern = re.compile(r'(\d+) (after|til) (\d+)')

def maketime(h,s):
    mytime = ''
    minutes = s / 60
    hour = (h + minutes/60 + 12) % 12
    if hour == 0: hour = 12
    minutes = str(minutes % 60)
    seconds = str(s % 60)
    if len(minutes) == 1:
        minutes = '0'+minutes
    if len(seconds) == 1:
        seconds = '0'+seconds
    return "{}:{}:{}".format(hour,minutes,seconds)


def maketimeneg(h,s):
    mytime = ''
    minutes = s / 60
    hour = h - 1 - minutes/60
    hour = hour + 24 % 12 
    if hour==0: hour = 12
    minutes = str(59 - (minutes % 60))
    seconds = str(59 - (s % 60))
    if len(minutes) == 1:
        minutes = '0'+minutes
    if len(seconds) == 1:
        seconds = '0'+seconds
    return "{}:{}:{}".format(hour,minutes,seconds)

with open(sys.argv[1],'r') as myinput:
    for line in myinput.read().split('\n'):
        if len(line) == 0: continue
        matches = pattern.findall(line)[0]
        degrees, direction, hour = matches
        degrees = int(degrees)
        hour = int(hour)
        angle = (12-hour) * 30
        if direction == 'after':
            notfound = False 
            for i in xrange(1,7200): # seconds
                minmove = i/10.
                hourmove = 30.*i/3600
                newangleint = int(angle - hourmove + minmove) % 360
                newangleflt = angle - hourmove + minmove
                if newangleflt < 0: newangleflt += 360
                if notfound and degrees == newangleint:
                    #print "{0}".format(newangleint),
                    print maketime(hour,i-1)
                    #print "{0:3.5f}".format(newangleflt)
                    break
                if newangleint != degrees:
                    notfound = True 
        if direction == 'til':
            found = False
            for i in xrange(1,7200): # seconds
                minmove = i/10.
                hourmove = 30.*i/3600
                #newangleint = int(angle + hourmove - minmove) % 360
                newangleflt = angle + hourmove - minmove - (1./30)
                newangleint = int(newangleflt) % 360
                if newangleflt < 0: newangleflt += 360
                if degrees - 1 <= newangleint <= degrees + 1:
                    print "Close: {0}".format(newangleint),
                    print maketimeneg(hour,i-1),
                    print "{0:3.5f}".format(newangleflt)
                    #break
                if found and newangleint != degrees:
                    print "{0}".format(newangleint), \
                            '{:f}'.format(newangleflt), newangleflt - newangleint,
                    print maketimeneg(hour,i-1)
                    #print "{0:3.5f}".format(newangleflt)
                    #break
                if newangleint == degrees:
                    found = True
