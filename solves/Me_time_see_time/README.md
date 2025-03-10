# Me_time_see_time

# Description

<p>You need to develop a small tool that looks at all the files in a directory with no subdirectories and prints out the files in order of the time they were last modified with the latest modified files on the top of the list. The file names will never exceed the initial column width. The input to your tool will be the path to the directory. Download the example data <a href="me_time_see_time_data1_tar.gz">Here</a>
</p>

## Sample Input:

```
$ ./me_time_see_time_solve.pl /path/to/dir/
```
## Expected Output:

```
$ ./me_time_see_time_solve.pl /path/to/dir/
FILENAME   MODIFIED TIME             CREATION TIME
temp0.txt  Sat Mar  5 15:51:49 2016  Sat Mar  5 15:51:54 2016
temp4.txt  Fri Mar 21 12:01:00 2014  Sat Mar  5 15:55:34 2016
temp2.txt  Mon Dec 17 15:33:00 2012  Sat Mar  5 15:54:18 2016
temp5.txt  Tue Nov 17 15:33:00 2009  Sat Mar  5 15:53:57 2016
temp1.txt  Mon Jan 17 15:33:00 2000  Sat Mar  5 15:54:35 2016
temp3.txt  Mon Oct 19 15:33:00 1998  Sat Mar  5 15:55:07 2016
```
## Expected SHA1 Hash:

```
480ffb6c127a16f072a8a1bdf6af3977b6fb173f
```
