# Tic_Tac_Toe_Show

## Sample Input:

```
$ cat tictactoe_input1.txt 
{
  "R1": {
    "X": [
      0,
      2
    ],
    "O": [
      0,
      0
    ]
  },
  "R2": {
    "X": [
      1,
      2
    ],
    "O": [
      2,
      2
    ]
  },
  "R3": {
    "X": [
      2,
      1
    ],
    "O": [
      1,
      1
    ]
  }
}
```
## Expected Output:

```
$ ./solve.py tictactoe_input1.txt 
['O', '*', 'X']
['*', 'O', 'X']
['*', 'X', 'O']
O Wins!
```
## Expected SHA1 Hash:

```
88212c50ab2fc978365bcea6184bcfe54d87abf3
```
