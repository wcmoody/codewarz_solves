# Hash_me_if_you_can

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called. Remember that the input will be one line with a period denoting the end of the string you need to find (but it is not part of the string).<br/><br/>
You will be given a string with missing characters (missing characters will already be replaced with an _) and the sha1 hash of the final string all in one line (the period is not part of the string you need to find).
Find the value of the final string. There will be four missing chars and will be composed of any combination of lower case letters, digits, punctuation and whitespace.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
this is a t_st str_ng a_d noth_ng more. sha1hash:01169074478b746b72722ea6238d5c5511465b5b
power_sdfasd_mkv as_dfljwqer_f. sha1hash:490e1a0ffd9f25e230f2dcedb272e71101f67c57


```
## Expected Output:

```
$ ./Hash_me_if_you_can_solve.py /path/to/somefile.txt
this is a test string and nothing more
powerasdfasdfmkv askdfljwqer f

```
## Expected SHA1 Hash:

```
497e9ded80d8ce5ae493040085ece194361bd4f0
```
