#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

lookup = {'Golf': 'G', 'bravo': 'b', 'india': 'i', 'Tango': 'T', 'echo': 'e',
'Xray': 'X', 'Whiskey': 'W', 'quebec': 'q', 'kilo': 'k', 'Sierra': 'S', 'lima':
'l', 'oscar': 'o', 'juliet': 'j', 'yankee': 'y', 'Mike': 'M', 'golf': 'g',
'Oscar': 'O', 'Hotel': 'H', 'Papa': 'P', 'tango': 't', 'Romeo': 'R', 'xray':
'x', 'whiskey': 'w', 'Delta': 'D', 'sierra': 's', 'Alpha': 'A', 'November': 'N',
'victor': 'v', 'Foxtrot': 'F', 'mike': 'm', 'Yankee': 'Y', 'zulu': 'z',
'Charlie': 'C', 'hotel': 'h', 'papa': 'p', 'uniform': 'u', 'romeo': 'r',
'delta': 'd', 'Victor': 'V', 'alpha': 'a', 'november': 'n', 'Uniform': 'U',
'foxtrot': 'f', 'Lima': 'L', 'Zulu': 'Z', 'charlie': 'c', 'India': 'I', 'Echo':
'E', 'Quebec': 'Q', 'Bravo': 'B', 'Kilo': 'K', 'Juliet': 'J'}

with open(sys.argv[1],'r') as myinput:
    text = myinput.read()
    for k,v in lookup.items():
        text = text.replace(k,v)
    text = text.replace('-','')
    print text
