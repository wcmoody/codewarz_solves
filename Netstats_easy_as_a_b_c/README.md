# Netstats_easy_as_a_b_c

# Description

<p>Your bosses have asked you to write a parsing program for netstat outputs. The host team has gone around and and collected outputs from the command "netstat -punta" on various machines. They want your program to take multiple command line arguments to parse the output file. They also want the output displayed in two sections, one with allowed/searching protocol and ports from the command line up top. Also anything that doesn't match the command line search options to be shown below. Pay really close attention to the examples (devil is in the details) as they give a clear indication of what is expected of your program. Example input file can be located <a href="/static/downloads/netstat_example1.txt">Here</a>
<br/><br/>
</p>

## Sample Input:

```
$ ./netstat_solve.py /path/to/netstat_example1.txt tcp:22
```
## Expected Output:

```
$ ./netstat_solve.py /path/to/netstat_example1.txt tcp:22
2: Allowed services/connections
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      2222/sshd
tcp        0      0 172.17.201.86:22        123.123.123.123:9999    ESTABLISHED 8877/sshd

4: Unknown services/connections
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:4444            0.0.0.0:*               LISTEN      1337/totally_legit
tcp        0      0 224.224.224.224:2222    123.123.123.123:22      ESTABLISHED 2277/sshd
tcp6       0      0 fe80::20c:29ff:fe37:25  :::*                    LISTEN      22/sendmail
udp6       0      0 :::31337                :::*                    LISTEN      12345/really_legit
```
## Expected SHA1 Hash:

```
ef5176ad24d74c93ff5a5b2ace539263bb677f7d
```
