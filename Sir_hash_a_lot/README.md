# Sir_hash_a_lot

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
<strong>Admin Note:</strong> On the server the english dictionary file is located at /usr/share/dict/american-english<br/><br/>
So your program can use that file path location in your uploaded program<br/><br/>
From the example hashes find the words that match the hash from the <a href="american-english">(/usr/share/dict/american-english)</a>, maybe the hashes are shifted?
<strong>ADMIN NOTES:</strong> About this challenge, due to the fact these are VM's and have limited memory. <strong>"DO NOT"</strong> attempt to pre build the entire possible combinations of all the hash types and all possible shifts. Do one at a time. We are able to get the the solve time down to 25 seconds on the VM. That's with solving both the example data set, and the server side data set. Locally on our laptops it took about 1 minute combined to solve both data sets. If your program cannot complete the example data set in under 1 min. Please do not upload your program.
<br/><br/>Challenge author: funtimes</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
q5r37o1n03r961m4n67qp44p6q9534p9n73665r9
6221fdec4d229fd08f08313gefcffd46e09031c78cg3907e5gbc7202
1s40sp92qn241694750979rr6ps582s2q5q7q28r18335qr05nop54q0560r0s5302860p652os08q560252nn5r74210546s369sooopr8p12psp7957o2652sr9n75
s7s30u6v4w8t864714sw46ts6uw3v5tt89t91rw4rt4w31vurt07tuw1w9090u4u
k7ii8k2758535jg182h4g5f396h22k3773288k3gh883j9k2j3i6f06jij3j89f06709780k23782f384j41fk36k5i2k4998h65k181gg4jg6j1i5kfij8h7fk60k51
```
## Expected Output:

```
$ ./sir_hash_alot_solve.py /path/to/somefile.txt
sir
hash
a
lot
electroencephalograph's
```
## Expected SHA1 Hash:

```
f5a9d47244dbdb38ee65cecba4a00f91512a292f
```
