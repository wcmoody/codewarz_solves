# Integers_and_IPs

# Description

<p>Did you know an ip address can be converted from an integer? Look through the provided sample file and find the appropriate integers to convert to its corresponding IP address</p>

## Sample Input:

```
$ cat sample1.txt 
this is only a test line with an ip address of 16777216

No. Time Source Destination Protocol Info
2 2009-06-04 07:15:26.734532 2886787088 217.112.94.230 HTTP GET /iehostcx32.dll HTTP/1.1
3 2009-06-04 07:15:27.960984 172.16.224.16 3648020198 HTTP GET /xpdeluxe.exe HTTP/1.1

and another
useless
test of lines

mysql&gt; select distinct count(*) as Count,mid(fw1time,12,5) as Time,fw1src from
fw1logs.20090605 where fw1time between "2009-06-05 09:00:00" and "2009-06-05 09:05:00"
and (fw1orig = 3232259958 or fw1orig = 3232258814 ) group by Time,fw1src order
by Count desc limit 5;
```
## Expected Output:

```
$ ./solve.py sample1.txt 
this is only a test line with an ip address of 1.0.0.0

No. Time Source Destination Protocol Info
2 2009-06-04 07:15:26.734532 172.16.224.16 217.112.94.230 HTTP GET /iehostcx32.dll HTTP/1.1
3 2009-06-04 07:15:27.960984 172.16.224.16 217.112.94.230 HTTP GET /xpdeluxe.exe HTTP/1.1

and another
useless
test of lines

mysql&gt; select distinct count(*) as Count,mid(fw1time,12,5) as Time,fw1src from
fw1logs.20090605 where fw1time between "2009-06-05 09:00:00" and "2009-06-05 09:05:00"
and (fw1orig = 192.168.95.118 or fw1orig = 192.168.90.254 ) group by Time,fw1src order
by Count desc limit 5;
```
## Expected SHA1 Hash:

```
855b70e97021685bb06db4d85e2fb0a969efaec7
```
