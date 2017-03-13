# Beer_run

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
You drew the short straw, and have been tasked to walk to the convenience store to buy more beer for your buddies. You have to figure out what is the shortest number of moves it takes to get to the store. There is a map given to you as a file input on where the store is. You must figure out how to get from the bottom left corner of the map(your starting point), and get to the convenience store(top right corner of the map) which is your end point. You can only move one block at a time either up, down, left, right. The "X's" represent a block that you cannot walk down. "O's" represent blocks you can walk down. Also there might be an instance to where there is no path to get to the store. If there is no path to the store, make sure you print the correct response as indicated in the example below.
<br/><br/>
</p>

## Sample Input:

```
$ cat /path/to/somefile2.txt
11
XOOOOXOOOOO
XOXXXXOOXOX
XOOOOOXOOOO
OOXOXOXOXXO
OOXOOOOOOOO
OOXOOOOOOOO
OOXOOOOOOOO
OOXOOOOOOOO
XOOXXXXXXXX
OOOOOOOOOOO
OOOOOOOOOOO
```
## Expected Output:

```
$ ./Beer_run_solve.py /path/to/somefile2.txt
24
```
## Expected SHA1 Hash:

```
4d134bc072212ace2df385dae143139da74ec0ef
```
