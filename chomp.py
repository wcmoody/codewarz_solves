#!/usr/bin/env python
import sys,hashlib; print(hashlib.sha1(sys.stdin.read().strip()).hexdigest())
