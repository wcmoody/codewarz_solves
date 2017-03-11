#!/usr/bin/env python
import sys
import re

usage = "%s <input_file> portocol:port ...." % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

ipv4 = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[\*0-9]+'

ipv6 = \
        r'(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(:?[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?:l:[0-9a-fA-F]{1,4}){1,4}|(:?[0-9a-fA-F]{1,4}:){1,2}(:?:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(:?(:?:[0-9a-fA-F]{1,4}){1,6})|:(:?(:?:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:?:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(:?ffff(:?:0{1,4}){0,1}:){0,1}(:?(:?25[0-5]|(:?2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(:?25[0-5]|(:?2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(:?[0-9a-fA-F]{1,4}:){1,4}:(:?(:?25[0-5]|(:?2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(:?25[0-5]|(:?2[0-4]|1{0,1}[0-9]){0,1}[0-9])' 

v6patt = \
r'([dtcpu6]+)\s+([0-9]+)\s+([0-9]+)\s+('+ipv6+r':[\*0-9]+)\s+('+ipv6+r':[\*0-9]+)\s+([A-Z]+)\s+([0-9]+\/[a-z_]+)'
#v6patt = ipv6+r"\:[0-9\*]+\s+"+ipv6+r"\:[i\*0-9]+"
v4patt = \
r'([dtcpu6]+)\s+([0-9]+)\s+([0-9]+)\s+('+ipv4+r')\s+('+ipv4+r')\s+([A-Z]+)\s+([0-9]+\/[a-z_]+)'

v6pattern = re.compile(v6patt)
v4pattern = re.compile(v4patt)

ippatt = \
'([dtcpu6]+)\s+([0-9]+)\s+([0-9]+)\s+(\S+:[\*0-9]+)\s+(\S+:[\*0-9]+)\s+([A-Z]+)\s+([0-9]+\/[a-z_]+)'

v6pattern = v4pattern = re.compile(ippatt)

protocols = {}
inputfile = sys.argv[1]
for protocol, port in [p.split(':') for p in sys.argv[2:]]:
    if protocol[:3] not in protocols.keys(): protocols[protocol[:3]] = []
    protocols[protocol[:3]].append(port)

allowed = []
unknown = []

with open(inputfile,'r') as myinput:
    lines = myinput.read().split('\n')[2:]
    for line in lines:
        if len(line) == 0: continue

        matches = v6pattern.findall(line)
        if len(matches) == 0:
            matches = v4pattern.findall(line)
        if len(matches) > 0:
            proto, recv, send, local, foreign, state, pidprog = matches[0]
            sport = local.split(':')[-1]
            dport = foreign.split(':')[-1]
            if proto[:3] in protocols.keys() and sport in \
                    protocols[proto[:3]]:
                allowed.append(matches[0])
            else:
                unknown.append(matches[0])

if len(allowed) > 0:
    pad1 = max([len(src[3]) for src in allowed])
    pad2 = max([len(dst[3]) for dst in allowed])
else: pad1 = pad2 = 0
if len(unknown) > 0:
    pad3 = max([len(src[3]) for src in unknown])
    pad4 = max([len(dst[3]) for dst in unknown])
else: pad3 = pad4 = 0
pad = max(pad1,pad2,pad3,pad4)

columns = "{:5} {:>6} {:>6} {:%d} {:%d} {:11} {}" % (pad+1, pad+1)
titles = ("Proto","Recv-Q","Send-Q","Local Address","Foreign Address","State",\
        "PID/Program name")
if len(allowed) > 0:
    print str(len(allowed)) + ": Allowed services/connections"
    print columns.format(*titles)

for a in allowed:
    print columns.format(*a)
print

if len(unknown) > 0:
    print str(len(unknown))+": Unknown services/connections"
    print columns.format(*titles)
for u in unknown:
    print columns.format(*u)
