#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)
"""
Dot = 10 Pts
Power Pellet = 50 Pts
1st Ghost = 200 Pts
2nd Ghost = 400 Pts
3rd Ghost = 800 Pts
4th Ghost = 1600 Pts
Cherry = 100 Pts - level 1 only
Strawberry = 300 Pts - level 2 only
Orange = 500 Pts - level 3 and 4 only
Apple = 700 Pts - level 5 and 6 only
Grapes = 1000 Pts - level 7 and 8 only
Galaxian = 2000 Pts - level 9 and 10 only
Bell = 3000 Pts - level 11 and 12 only
Key = 5000 Pts - level 13 and higher
"""
dot = 10
powerpellet = 50
ghosts = {}
ghosts[0] = 200
ghosts[1] = 400
ghosts[2] = 800
ghosts[3] = 1600

dot_count = 240
power_count = 4
energizers = power_count * sum(ghosts.values())

cherry = 100
strawberry = 100
orange = 500
apple = 700
grapes = 1000
galaxian = 2000
bell = 3000
key = 5000

noeatghost = range(19,1000) + [17]

items = {1:cherry, 2:strawberry, 3:orange, 4:orange, 5:apple}
items[6]= apple
items[7] = items[8] = grapes
items[9] = items[10] = galaxian
items[11] = items[12] = bell
for i in xrange(257):
    items[13+i] = key

maxscores = {}
maxscores[0] = 0
for i in xrange(1,257):
    maxscores[i] =  maxscores[i-1] + (dot_count*dot)
    maxscores[i] += 2 * items[i]
    if i not in noeatghost:
        maxscores[i] += energizers
    maxscores[i] += power_count * powerpellet

#for k, v in maxscores.items():
#    if k<250 : print k, v

output = []
with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        score = int(line)
        for k,v in maxscores.items():
            if v > score:
                output.append((score,k))
                #print "%d Level: %d" % (score,k)
                break

highscore = max([s[0] for s in output])
spacing = len(str(highscore)) + 1
myformat = "{:>%dd} Level: {}" % (spacing)
for score, level in output:
    print myformat.format(score, level)

