#!/usr/bin/env python
import sys
import json

usage = "%s <input_file>" % sys.argv[0]

if len(sys.argv) < 2:
    exit(usage)

board = [['*','*','*'],['*','*','*'],['*','*','*']]


def winner():
    #check rows
    for row in board:
        if all([row[i] == 'X' for i in range(3)]):
            return "X Wins!"
        if all([row[i] == 'O' for i in range(3)]):
            return "O Wins!"
    #check columns
    for x,y,z in zip(*board):
        if all([c == 'X' for c in [x,y,z]]):
            return "X Wins!"
        if all([c == 'O' for c in [x,y,z]]):
            return "O Wins!"
    #check diagonals
    if all([board[d][d] == 'X' for d in range(3)]):
        return "X Wins!"
    if all([board[d][d] == 'O' for d in range(3)]):
        return "O Wins!"

    if all([board[d][2-d] == 'X' for d in range(3)]):
        return "X Wins!"
    if all([board[d][2-d] == 'O' for d in range(3)]):
        return "O Wins!"
    return "Draw!"



with open(sys.argv[1],'r') as myinput:
    data = myinput.read()

game = json.loads(data)

result = "Draw!"

for r, moves in game.items():
    for p,coords in moves.items():
        x, y = coords
        board[x][y] = str(p)
    result = winner()
    if result != "Draw!":
        break

for row in board:
    print row
print result



