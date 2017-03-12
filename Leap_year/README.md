# Leap_year

## Sample Input:

```
$ cat samplefile
2004 2008 1896-1900
2012
1995-1997 1998-2000
```
## Expected Output:

```
$ ./solve.py /path/to/samplefile
1896: True
1897: False
1898: False
1899: False
1900: False
1995: False
1996: True
1997: False
1998: False
1999: False
2000: True
2004: True
2008: True
2012: True
```
## Expected SHA1 Hash:

```
03bf483cbd017aa5720da063920302a87cafccbf
```
