import re
valid = '[C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC]'.replace(':','|')
valid = valid.replace('[','').replace(']','')
lineLength = raw_input()
for i in range(1, int(lineLength)+1):
    Regex_Pattern1 = (r'^\d{4,5}\s%s$' % valid)
#    Regex_Pattern1 = r'^\d{4,5}\s%s' % valid
    patt = re.compile(Regex_Pattern1)
    testString = raw_input()
    if bool(re.search(Regex_Pattern1, testString)):
        print('VALID')
    else:
        print('INVALID')
