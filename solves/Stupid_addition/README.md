# Stupid_addition

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
Well it seems we have been tasked with adding numbers from a text file, however it seems Ray Charles was the data entry clerk typing on the keyboard and couldn't see the typos he made on the input data. Develop a program that attempts to add two numbers from a line and give the correct output. Be sure to gracefully deal with non-standard input.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
1 1
2 2
3 3
a a
b b
c c
1 a
a 1
-1 2
2 -1
1.1 2.3
9.1
9.a
9.(
9.)
-9(
0.1 0.2
```
## Expected Output:

```
$ ./stupid_addition_solve.py /path/to/somefile.txt
2
4
6
1
1
3.4
0.3
```
## Expected SHA1 Hash:

```
1bebfc6ee4d6699b8843979cfe09ed64ed869d0c
```
