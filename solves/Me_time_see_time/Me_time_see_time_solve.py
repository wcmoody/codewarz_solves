#!/usr/bin/env python
import sys
from os import listdir
from os.path import isfile, join, getmtime as mt, getctime as ct
from time import ctime as c
from operator import itemgetter


usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

fileinfo = {}
pathtodir = sys.argv[1]
files = [f for f in listdir(pathtodir) if isfile(join(pathtodir,f))]
for f in [join(pathtodir,fx) for fx in files]:
    fileinfo[f.split('/')[-1]] = (mt(f), ct(f)) 

longname = max(len(filename) for filename in fileinfo.keys())
#header =  "FILENAME" + ' '*(longname-7+1) + "MODIFIED TIME" + 13*' '
header = "FILENAME   MODIFIED TIME             CREATION TIME"
print header

sorted_files = sorted(fileinfo.items(), key=itemgetter(1), reverse=True)
for f in sorted_files:
    output = "{:<11s}".format(f[0])
    output += c(f[1][0])+"  " + c(f[1][1])
    print output
