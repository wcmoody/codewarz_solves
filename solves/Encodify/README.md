# Encodify

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.
<br/><br/>
<strong>Admin Note:</strong> On the server the english dictionary file is located at /usr/share/dict/american-english<br/>check plaintext first ;)<br/>
So your program can use that file path location in your uploaded program<br/><br/>
Each word of a line in an input file is either base64-encoded, rot-13 encoded, both, or neither in no particular order. Decode the message and return all english-language (human-readable) words
<a href="https://codewarz.ninja/static/downloads/american-english.txt">(/usr/share/dict/american-english)</a>. Any numbers should be left as they are.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
This aXM= n c2hhYWw= p3ElnJ5a jhgjhg
```
## Expected Output:

```
$ ./Encodify_solve.py /path/to/somefile.txt
This is a funny string
```
## Expected SHA1 Hash:

```
8790b3d81a5b759603c1e3a48cd3ea540f8f131e
```
