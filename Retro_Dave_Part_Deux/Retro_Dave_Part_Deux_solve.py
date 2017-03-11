#!/usr/bin/env python
import sys
from operator import itemgetter
from csv import DictReader
from csv import reader

usage = "%s <input_file1> <input_file2>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

with open(sys.argv[1]) as f:
    gameboy = reader(f)
    gameboy = list(gameboy)

with open(sys.argv[2]) as f:
    gbcolor= reader(f)
    gbcolor = list(gbcolor)

master = []
for game in gameboy[1:]:
    title, released = game[0], game[2]
    if len(released) == 0: continue
    master.append([title,released, "Game Boy"])

for game in gbcolor[1:]:
    title, released = game[0], game[2]
    if len(released) == 0: continue
    master.append([title,released, "Game Boy Color"])

games = sorted(master, key = lambda g: (g[1], g[0]))

for game in games:
    title = game[0]
    released = game[1]
    platform = game[2]
    if len(title) >= 15:
        title = title[:14] + '~'
    print "{:>15} {} {:>14}".format(title,released,platform)
