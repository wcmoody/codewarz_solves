#!/usr/bin/env python
import sys
import os
import re

usage = "%s <path/to/dir>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)


patstr = """\
/+----------------------------------/+
|             rubric               |
/+----------------/+---------/+-------/+
|                | maximum | score |
/+----------------/+---------/+-------/+
| correct        |   (\d+)%   |  (\d+)%  |
/+----------------/+---------/+-------/+
| readable       |   (\d+)%   |  (\d+)%  |
/+----------------/+---------/+-------/+
| efficient      |   (\d+)%   |  (\d+)%  |
/+----------------/+---------/+-------/+
| writeup        |   (\d+)%   |  (\d+)%  |
/+----------------/+---------/+-------/+
"""
correctstr = "(\|\s*correct\s*\|\s*(\d{1,3})%\s*\|\s*(\d{1,3})%\s*\|)"
correct = re.compile(correctstr)
readablestr = "(\|\s*readable\s*\|\s*(\d{1,3})%\s*\|\s*(\d{1,3})%\s*\|)"
readable = re.compile(readablestr)
efficientstr = "(\|\s*efficient\s*\|\s*(\d{1,3})%\s*\|\s*(\d{1,3})%\s*\|)"
efficient = re.compile(efficientstr)
writeupstr = "(\|\s*writeup\s*\|\s*(\d{1,3})%\s*\|\s*(\d{1,3})%\s*\|)"
writeup = re.compile(writeupstr)


directories = os.walk(sys.argv[1])

next(directories)

titlepattern = re.compile("([a-zA-Z]*)(\d*)")

all_students = []
for directory in directories:
    all_students.append(directory)

students = sorted(all_students, key=lambda e: e[0])

for student in students:
    files = student[2]
    for f in files:
        heading = student[0].split('/')[-1]
        #number = heading[len('student'):]
        #print "student" + number.lstrip('0')
        #print heading
        print f.split('_')[0]
        with open(student[0] +"/"+f) as fd:
            data = fd.read()
            c = correct.findall(data)
            r = readable.findall(data)
            e = efficient.findall(data)
            w = writeup.findall(data)
            if c and r and e and w:
                print c[0][0]
                print r[0][0]
                print e[0][0]
                print w[0][0]
                total = sum(int(x[0][2]) for x in [c,r,e,w])
                print "Total: %d%%" % total
                print
