#!/usr/bin/env python
import sys
from PIL import Image
import re

print re.findall(r'(CWN\{[^\}]*\})',''.join([chr(p[2]) for p in Image.open(sys.argv[1]).transpose(Image.ROTATE_90).transpose(Image.FLIP_TOP_BOTTOM).getdata()]))[0]
