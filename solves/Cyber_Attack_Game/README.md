# Cyber_Attack_Game

# Description

<p>This guy (also known as funtimes) developed his own custom game with various cyber attacks. Certain cyber attacks are more powerful than others, so it wins when compared to another type of attack. Given the example data and output, can you figure out the pattern and primacy and recreate his scoring engine based on an input file being fed into your program. It also appears that if a player doesn't give a correct attack type, or if a player wins, all subsequent plays for that round do not matter.</p>

## Sample Input:

```
$ cat samplefile
1e ee
ee ee ee ee ee ee ee
ee ee ec ee ee ee ee e1
cc ec
ei ei ei ei
es se
ce ee
cc ss
11 ei ec ce
ci ec
cs ci
ie ce
ic ii
ii ii
is ic
se
sc
si
ss
e1 cc
```
## Expected Output:

```
$ ./solve.py /path/to/samplefile
Illegal move by Player 1!
Draw!
Player 2 Wins!
Player 2 Wins!
Player 2 Wins!
Player 1 Wins!
Player 1 Wins!
Draw!
Illegal moves by both players!
Player 2 Wins!
Player 2 Wins!
Player 1 Wins!
Player 1 Wins!
Draw!
Player 1 Wins!
Player 2 Wins!
Player 1 Wins!
Player 2 Wins!
Draw!
Illegal move by Player 2!
```
## Expected SHA1 Hash:

```
5a8995aaaad38134e64f8a98c477acf66506ac17
```
