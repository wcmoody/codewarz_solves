# Flava_flav

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
Tim Jones is a bit of a nerd. Check that – he’s a HUGE nerd. When you ask him the time, he might say something like “20 after 8”, which seems normal, but other times he’ll say things like “90 after 8” or “126 til 4”.<br/><br/>
When you ask him about this, Tim say that “20 after 8” means the first time after 8 that the hour and minute hands of the clock make an angle of 20 degrees; “126 til 4” means the closest time before 4 that the hands make an angle of 126 degrees. <br/><br/>
As Tim walks away, you resolve that you will write a program that will automatically convert his times to our more normal, non-nerdy times.<br/><br/>
Input<br/><br/>
Each test case consists of a single line of the form a after b or a til b, where a and b are integers satisfying 0 &lt;= a &lt;= 360, and 1 &lt;= b &lt;= 12. All angles are measured starting at the hour hand and moving clockwise until reaching the minute hand.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
20 after 8
126 til 4
180 til 1
0 after 12
```
## Expected Output:

```
$ ./Flava_flav_solve.py /path/to/somefile.txt
8:47:16
3:39:16
12:32:44
1:05:27
```
## Expected SHA1 Hash:

```
c234887b15e9ea3ff1c127222d39fa57255f8cc9
```
