# Yet_another_encoding

# Description

<p>The script-kiddies keep trying to sneak data outside of your network with his own encoding schemes as to not get caught by normal IDS sensors. Can you break his encoding scheme and decode the message?</p>

## Sample Input:

```
$ cat samplefile
ad d5 n cd 4 88 r a2 86 a6 8a bc e 9e 86 a6 4 a4 j d3 aa a6 86 d5 8c bc
```
## Expected Output:

```
$ ./solve.py /path/to/samplefile
LoCk SEcReTs
aRe dAngeRoUs
```
## Expected SHA1 Hash:

```
99ed2530b09cfb9e1eee43b009437eedaa879dc3
```
