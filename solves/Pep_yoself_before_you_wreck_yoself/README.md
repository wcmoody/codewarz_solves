# Pep_yoself_before_you_wreck_yoself

# Description

<p>Coworkers spend an inordinate amount of time ridiculing your code for not following <a href="https://www.python.org/dev/peps/pep-0008/">PEP8</a> standards. They say hurtful things like: "Your code is not very Pythonic" and "Go back to the stone age and keep programming in Java". You vow to show them and write a PEP8 checker for your own programs. After perusing the entire PEP8 document you decide to start small and only focus on the following PEP8 standards by using the associated check description:<br/>
1. <a href="https://www.python.org/dev/peps/pep-0008/#maximum-line-length">Line length</a> yo man, this line is ,long (X &gt; 79 characters)<br/>
2. <a <="" a="" href="https://www.python.org/dev/peps/pep-0008/#imports&gt;One import"> per line come on! keep these one to a line<br/>
3. </a><a href="https://www.python.org/dev/peps/pep-0008/#block-comments">Block comments</a> shouldn't there be a hashtag AND a space?<br/>
4. <a href="https://www.python.org/dev/peps/pep-0008/#inline-comments">Inline comments</a> gimme gimme gimme 2 spaces for inline comment<br/>
5. <a href="https://www.python.org/dev/peps/pep-0008/#indentation">4 spaces</a> per indentation level quad spaces FTW<br/>
6. <a href="https://www.python.org/dev/peps/pep-0008/#other-recommendations">Trailing whitespace</a> Trailing hEx 20 yo<br/>
7. <a href="https://www.python.org/dev/peps/pep-0008/#blank-lines">Surrounding top-level functions</a> two yes! one no!<br/>
<br/><br/>
If your codes fails the PEP8 check it should print the filename, line number, and check description in the following format.</p>

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
