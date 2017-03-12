# Pep_yoself_before_you_wreck_yoself

## Sample Input:

```
$ cat non_pep0.py
#!/usr/bin/env python3

import re, string
import copy

def long_func():  # this line is not crap
   print('This is totally a legit line for Python. It does violate the pep8 standard....HOW DARE YOU!!!')

def main(): #this line is crap
    print ('this is not the pep you are looking for!')
    long_func()

#comments are cool and probably mean something only if they are readable and stuffs
if __name__ == '__main__':   
   main()
```
## Expected Output:

```
$ ./solve.py /path/to/non_pep0.py
/full/path/to/non_pep0.py    3 come on! keep these one to a line
/full/path/to/non_pep0.py    6 two yes! one no!
/full/path/to/non_pep0.py    7 yo man, this line is long (105 &gt; 79 characters)
/full/path/to/non_pep0.py    7 quad spaces FTW
/full/path/to/non_pep0.py    9 shouldn't there be a hashtag AND a space?
/full/path/to/non_pep0.py    9 gimme gimme gimme 2 spaces for inline comment
/full/path/to/non_pep0.py    9 two yes! one no!
/full/path/to/non_pep0.py   13 yo man, this line is long (83 &gt; 79 characters)
/full/path/to/non_pep0.py   13 shouldn't there be a hashtag AND a space?
/full/path/to/non_pep0.py   14 Trailing hEx 20 yo
/full/path/to/non_pep0.py   15 quad spaces FTW
```
## Expected SHA1 Hash:

```
5f7d24d179cac58936f4416f61ce11ecb35582f3
```
