# Stack_the_stacking_stackers

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
You need to write a program that can validate input and return True based on two criteria and False if it violates either criteria:<br/>
1. There are an identical number of 0's and 1'.<br/>
2. That for every 0, there is a single 1 that appears after it.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
000111

111000

01

1001

0011

1

010101
```
## Expected Output:

```
$ ./Stack_the_stacking_stackers.py /path/to/somefile.txt
True
False
True
False
True
False
True
```
## Expected SHA1 Hash:

```
fc20a81b64d986a655fe01ffc927126f94da3b20
```
