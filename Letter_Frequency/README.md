# Letter_Frequency

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
Your program should (excluding all non-alphabetic characters) display two lists, the first containing the set of unique letters in the order that it appears in the text, and the second representing the respective counts of each letter in the message. Input files spanning multiple lines should all be considered part of the same data-set, ie; your program should output the total letter counts for every line in the file just once (not for each line).
<br/><br/>
</p>

## Sample Input:

```
$ cat /path/to/somefile2.txt
'Two plus two equals four. wwwwwwww'
```
## Expected Output:

```
$ ./Letter_frequency_solve.py /path/to/somefile2.txt
letters:   t,    w,    o,    p,    l,    u,    s,    e,    q,    a,    f,    r
counts:    2,   10,    3,    1,    2,    3,    2,    1,    1,    1,    1,    1
```
## Expected SHA1 Hash:

```
e462766597c0b8a104ae4b1eb5b3bed083e159f0
```
