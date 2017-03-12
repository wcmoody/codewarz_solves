# Its_new_math

## Sample Input:

```
$ cat samplefile
13 = 14 - 1
2 * 2 = 4
1 * 1 = 1
10 + b = 22
96 = 24 + 6 / 3 * 5 * 8 - 9
24 + 6 / (3 * 5) * 8 - 9 = 15
0 / 5 = 0
5 / 0 = 0
99 = 98 + 1
5 = 2 + 2
2 + 2 = 4
-2 + -1.75 = -3.75
-100.0001 = -101 - 1
-100.0001 = -101 - -0.9999
```
## Expected Output:

```
$ ./solve.py /path/to/samplefile
True:   13 = 14 - 1
True:   2 * 2 = 4
True:   1 * 1 = 1
Error:  10 + b = 22
False:  96 = 24 + 6 / 3 * 5 * 8 - 9
True:   24 + 6 / (3 * 5) * 8 - 9 = 15
True:   0 / 5 = 0
Error:  5 / 0 = 0
True:   99 = 98 + 1
False:  5 = 2 + 2
True:   2 + 2 = 4
True:   -2 + -1.75 = -3.75
False:  -100.0001 = -101 - 1
True:   -100.0001 = -101 - -0.9999
```
## Expected SHA1 Hash:

```
ae004482cb7de668aede8cba2862d5b8adb3d3d4
```
