# coding: utf-8
import re
patt = re.compile("tom|jerry")
test = "tomtomjerrytomjerry"
print patt.findall(test)
