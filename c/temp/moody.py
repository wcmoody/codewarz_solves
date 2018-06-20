# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = sys.stdin.readlines()[1:]

valids = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC".split(':')


for d in data:
    if ' ' not in d: continue
    code, language = d.split(' ')
    if language.strip() in valids and 1000 <= int(code) <= 99999:
        print "VALID"
    else:
        print "INVALID"
