# IP_Finder_and_Validator

# Description

<p>Given a log file, grab as many IP addresses (4 octet numbers) as you can and push those numbers through an IP address validator to verify their correctness. Print out if they are valid or not. Keep track of how many times you see each IP address. Pay close attention to the example output for the formatting and ordering details.
<br/>
Example input: <a href="ip_finder_and_validator_data1.txt">ip_finder_and_validator_data1.txt</a>
</p>

## Sample Input:

```
$ ./ip_truthiness.pl /path/to/ip_finder_and_validator_data1.txt

```
## Expected Output:

```
$ ./ip_truthiness.pl /path/to/ip_finder_and_validator_data1.txt
(001) False:       7.888.8.8 *
(001)  True:     11.11.11.95 *
(001)  True:    11.11.11.105 *
(001)  True:    24.17.237.70 *
(001)  True:   141.101.97.63 *
(001)  True:   141.101.98.43 *
(001)  True:   141.101.98.53 *
(001)  True:   141.101.98.63 *
(001)  True:  141.101.198.63 *
(001) False:       444.2.2.2 *
(001) False:       555.1.1.1 *
(002)  True:         2.2.2.2 *
(002) False:     09.01.02.03 *
(002)  True:   141.102.98.63 *
(003)  True:     11.11.11.89 *
(003)  True:   141.101.98.61 *
(004)  True:     11.11.11.70 *
(004)  True:  192.150.249.87 *
(004)  True:  211.168.230.94 *
(045)  True:       127.0.0.1 *
(049)  True:  211.190.205.93 *
(050)  True:    61.73.94.162 **
```
## Expected SHA1 Hash:

```
0fdc77bb4222a0cf54dd8eae96562ad36926ac60
```
