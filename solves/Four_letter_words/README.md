# Four_letter_words

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
<strong>Admin Note:</strong> On the server the english dictionary file is located at /usr/share/dict/american-english<br/><br/>
So your program can use that file path location in your uploaded program<br/><br/>
Given a file with a bunch of hashes in it (sha what?), find and print the 4 character english-american <a href="https://codewarz.ninja/static/downloads/american-english.txt">(/usr/share/dict/american-english)</a> words that correspond to each. If it's not a word, don't print it.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
4a91ee5f0106c2b35c11c168352f0abfbf4fc86165c62d6fb51b5232dfc692e6
26bb606a99df12a74752e5fc5a534c0f7a565a33be73db28f5dd0cab7edeed9c
4830d6003188a19785d44568765e1aa3da02677670dea10c09027604b7aa864b
70d6fb82261e9f4bcedfd8203d5b2a3b2eb7fe366076c065dfc309ee9398a68d
22ef82489ab58006f1e8dbeeb0b8b1bb091877af754896358960f1b5860eac02
```
## Expected Output:

```
$ ./four_letter_words_solve.py /path/to/somefile.txt
area
puny
```
## Expected SHA1 Hash:

```
d01a82b3c0643d7f5f0dfaf1536905fb15731fc5
```
