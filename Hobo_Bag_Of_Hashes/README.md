# Hobo_Bag_Of_Hashes

# Description

<p>After reading some open source reports out on the interwebs, the reports listed some hashes of files know to be tied to a particular dumb user who likes to carry his expensive macbook in a hobobag. Can you implement a way of finding the files if we give you the hash?<br/><br/>
Example files found <a href="/static/downloads/hobo_hashing_files.tgz">here</a> and <a href="/static/downloads/hobo_hashes.txt">here</a></p>

## Sample Input:

```
$ cat hobo_hashes.txt
cbd2657be030c81df3f4f91c5d9a86c63e26603c4ee89b9893e7feefe6e9d8c7f8a43926d01cee9cfe77789a3ff006f8372571f86248b6514147576b6fd2d04b
f572d396fae9206628714fb2ce00f72e94f2258f
01faf82ec0851559afe1a10fbfe017db5c7bc3ed2ce4a93cee95c780939f4d41
d144b8af3d8f991bf90ed26d4ac2fc93
2454c965b26013e1c3a0cb9275a5a5ab3c04f5106e510ed80a67caaeff43c088787076183176c01f358ae0a6361c5883
49debbc252b465110ddfc03c6f16c2a6dd67ee625271474e0627a1ea
```
## Expected Output:

```
$ ./solve.py hobo_hashes.txt /tmp/files/hash_test/
Found the file /tmp/files/hash_test/file9.txt with the hash of cbd2657be030c81df3f4f91c5d9a86c63e26603c4ee89b9893e7feefe6e9d8c7f8a43926d01cee9cfe77789a3ff006f8372571f86248b6514147576b6fd2d04b
Found the file /tmp/files/hash_test/file1.txt with the hash of f572d396fae9206628714fb2ce00f72e94f2258f
Found the file /tmp/files/hash_test/file10.txt with the hash of 01faf82ec0851559afe1a10fbfe017db5c7bc3ed2ce4a93cee95c780939f4d41
Found the file /tmp/files/hash_test/file4.txt with the hash of d144b8af3d8f991bf90ed26d4ac2fc93
Found the file /tmp/files/hash_test/file7.txt with the hash of 2454c965b26013e1c3a0cb9275a5a5ab3c04f5106e510ed80a67caaeff43c088787076183176c01f358ae0a6361c5883
Found the file /tmp/files/hash_test/file2.txt with the hash of 49debbc252b465110ddfc03c6f16c2a6dd67ee625271474e0627a1ea
```
## Expected SHA1 Hash:

```
a7d47d279972b1d19edc4dbcb4fc2591d2cc8fab
```
