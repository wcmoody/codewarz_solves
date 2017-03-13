# Achy_breaky_new_lines

# Description

<p>The weird country singer with a mullet can't figure out how to get rid of all these extra lines between his song lyrics. He has asked that you write a program that gets rid of all the extra new lines, so he can save on printer paper.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
But don't tell my new lines

My achy breaky new lines


I just don't think he'd understand



And if you tell my new lines




My achy breaky new lines





He might blow up and kill this man
```
## Expected Output:

```
$ ./achy_break_new_lines_solve.py /path/to/somefile.txt
But don't tell my new lines
My achy breaky new lines
I just don't think he'd understand
And if you tell my new lines
My achy breaky new lines
He might blow up and kill this man
```
## Expected SHA1 Hash:

```
adebf18da1758f7ab730f9f999ef85b5a01458b5
```
