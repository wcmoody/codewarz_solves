#!/usr/bin/env python
import sys

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))


def buildgraph(lines):
    graph = {}
    for (y,line) in enumerate(lines):
        for (x,char) in enumerate(line):
            if char == 'X': continue
            key = "%d-%d" % (x,y)
            value = set()
            neighbors = []
            left, right, top, bottom = False, False, False, False 
            if x==0: left = True 
            if x==len(lines)-1: right = True
            if y==0: top = True
            if y==len(lines)-1: bottom = True
            if not bottom: neighbors.append((0,1))
            if not top: neighbors.append((0,-1))
            if not right: neighbors.append((1,0))
            if not left: neighbors.append((-1,0))
            for (x1,y1) in neighbors:
                if lines[y+y1][x+x1] == "O":
                    value.add("%d-%d" % (x+x1,y+y1))
            graph[key] = value
    return graph
 
with open(sys.argv[1],'r') as myinput:
    lines = myinput.read().split('\n')
    while len(lines[-1]) == 0:
        lines.pop(len(lines)-1)
    dim = int(lines[0])
    for line in lines[1:]:
        if len(line) == 0: continue
        for item in line:
            if not all(c in ('X','O') for c in line):
                exit("Error: invalid character in file")
    graph = buildgraph(lines[1:])
    begin = "%d-%d"%(0,dim-1)
    end = "%d-%d" % (dim-1,0)
    if end in bfs(graph,begin):
        print len(bfs_paths(graph,begin,end))-1
    else:
        print "Puzzle cannot be solved!"
