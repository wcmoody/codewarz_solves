#!/usr/bin/python
import os
import sys

usage = "usage: %s <path_to_binary>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

filename = sys.argv[1]

current = os.listdir()


