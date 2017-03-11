#!/usr/bin/env python
import sys
from operator import itemgetter
from csv import DictReader
from csv import reader

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


with open(sys.argv[1]) as f:
    nes = reader(f)
    games = list(nes)

games = sorted(games[1:], key = lambda g: (g[2], g[0]))

for game in games:
    title = game[0]
    released = game[2]
    if len(title) >= 15:
        title = title[:14] + '~'
    print "{:>15} {}".format(title,released)
