# Making_Lists_Hard

## Sample Input:

```
$ cat input0.txt 
1
a
2
3
4
5,b,6,7,c,8
9
10
d
11
e
12,13,f,14,15,h,16,17
18
19
20
i
```
## Expected Output:

```
$ ./break_list.py input0.txt 
[1, 2, 3, 4, [5, 6, 7, 8], 9, 10, 11, [12, 13, 14, 15, 16, 17], 18, 19, 20]
```
## Expected SHA1 Hash:

```
0a4a6e81c39a953a751264f86964a349f2e9f769
```
