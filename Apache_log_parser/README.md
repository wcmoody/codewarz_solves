# Apache_log_parser

# Description

<p>Create a histogram from the apache log excerpts based on <strong>valid IPv4 ip-addresses</strong>. Also it might help to know that IP address can also appear in more than one place. They can be at the beginning of each line, and also in the middle as a requested url. But we only care about the ones at the beginning of each line.
<br/><br/><a href="/static/downloads/apache_log_parser_data1.txt">download the sample data file here</a></p>

## Sample Input:

```
$ ./apache_log_parser_solve.py /path/to/apache_log_parser_data1.txt
```
## Expected Output:

```
$ ./apache_log_parser_solve.py /path/to/apache_log_parser_data1.txt
        1.2.3.4: ***** (5)
        6.6.6.6: **** (4)
        5.6.7.8: **** (4)
        9.1.2.3: *** (3)
244.244.244.244: ** (2)
        7.6.6.6: ** (2)
        6.7.6.6: ** (2)
        6.6.7.6: ** (2)
        6.6.6.7: ** (2)
        1.2.3.0: ** (2)
255.255.255.255: * (1)
255.255.254.255: * (1)
       11.5.6.7: * (1)
       10.3.4.5: * (1)
     10.0.0.255: * (1)
       10.0.0.1: * (1)
        9.1.2.4: * (1)
        9.1.2.1: * (1)
        1.2.3.6: * (1)
        1.2.3.5: * (1)
        1.2.3.1: * (1)
```
## Expected SHA1 Hash:

```
824fb7483cf374460c7902aef69c63377bc21c44
```
