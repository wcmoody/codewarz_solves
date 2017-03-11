#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

moves = "ecsi"
attacks = {'ec':2 ,'ce':1, 'es':1, 'se':2, 'ic':1, 'ci':2, 'ei':2, 'ie':1,
        'cs':2 , 'sc':1, 'si':2, 'is':1}

with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    for line in lines:
        if len(line) == 0: continue
        index = lines.index(line)
        rounds = line.split(' ')
        for i, rnd in enumerate(rounds):
            if rnd[0] not in moves and rnd[1] not in moves:
                print "Illegal moves by both players!"
                break
            if rnd[0] not in moves:
                print "Illegal move by Player 1!"
                break
            if rnd[1] not in moves:
                print "Illegal move by Player 2!"
                break
            if rnd in attacks.keys():
                print "Player %d Wins!"% attacks[rnd]
                break 
            if i == len(rounds)-1: 
                print "Draw!"

            



