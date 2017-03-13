# Symmetric_Addition

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
Given a list of integers, write a program that creates and returns a NEW list with the same number of elements as the original list, such that each integer in the new list is the sum of itself and the location in the list that is symmetric to it. In other words, the first element is added to the last element, the second element is added to the second to last element, and so forth.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
[1,2,3,7,4]
[1,5,3,11,7,9]
```
## Expected Output:

```
$ ./Symmetric_Addition_solve.py /path/to/somefile.txt
[5, 9, 3, 9, 5]
[10, 12, 14, 14, 12, 10]
```
## Expected SHA1 Hash:

```
293052966b8af2b6435ef8b1ac66aa9e5c217ef4
```
