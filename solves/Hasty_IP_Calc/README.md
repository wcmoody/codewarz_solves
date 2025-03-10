# Hasty_IP_Calc

# Description

<p>A sysadmin in this shop has a bunch of config files with a IP address/cidr notation and gateway address per line. Can you help validate the gateway address is correct given the network address space? Also make sure to follow the output format as seen from the example.</p>

## Sample Input:

```
$ cat input1.txt 
172.16.0.0/12 172.16.0.1
172.16.0.0/16 172.17.0.1
10.100.0.0/16 10.100.255.255
10.100.0.0/16 10.100.0.0
10.100.0.0/16 10.100.0.1
192.168.10.0/24 192.168.1.1
8.0.0.0/13 8.1.100.255
```
## Expected Output:

```
$ ./solve.py input1.txt 
Network: 172.16.0.0
Total usable IP's: 1048574
Usable range: 172.16.0.1-31.255.254
Broadcast Address: 172.31.255.255
Gateway Address: 172.16.0.1

Network: 172.16.0.0
Total usable IP's: 65534
Usable range: 172.16.0.1-255.254
Broadcast Address: 172.16.255.255
Gateway Address: Invalid

Network: 10.100.0.0
Total usable IP's: 65534
Usable range: 10.100.0.1-255.254
Broadcast Address: 10.100.255.255
Gateway Address: Invalid

Network: 10.100.0.0
Total usable IP's: 65534
Usable range: 10.100.0.1-255.254
Broadcast Address: 10.100.255.255
Gateway Address: Invalid

Network: 10.100.0.0
Total usable IP's: 65534
Usable range: 10.100.0.1-255.254
Broadcast Address: 10.100.255.255
Gateway Address: 10.100.0.1

Network: 192.168.10.0
Total usable IP's: 254
Usable range: 192.168.10.1-254
Broadcast Address: 192.168.10.255
Gateway Address: Invalid

Network: 8.0.0.0
Total usable IP's: 524286
Usable range: 8.0.0.1-7.255.254
Broadcast Address: 8.7.255.255
Gateway Address: 8.1.100.255
```
## Expected SHA1 Hash:

```
63ceb53e882e7c3fc249b4fe8658a5bf5450dd40
```
