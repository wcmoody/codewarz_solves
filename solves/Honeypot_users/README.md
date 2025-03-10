# Honeypot_users

# Description

<p>Your boss has given you the task of finding all username &amp; password attempts on the honeypot in the company DMZ. Pay careful attention to the output format/ordering of the data. Also take note that if the username or password attempt has a "/" in it, then you must discard that entry.<br/><br/>
Example files found <a href="honeypot_examples_logs.tgz">here</a></p>

## Sample Input:

```
$ ./solve.py /path/to/logfilesdirectory/
```
## Expected Output:

```
$ ./solve.py /path/to/logfilesdirectory/
User account "PlcmSpIp" has been attempted "1" times overall.
    Password "&lt;Any pass&gt;" was attempted 1 times.
User account "service" has been attempted "1" times overall.
    Password "service" was attempted 1 times.
User account "administrator" has been attempted "2" times overall.
    Password "1234" was attempted 2 times.
User account "shell\x00" has been attempted "2" times overall.
    Password "sh\x00" was attempted 2 times.
User account "enable\x00" has been attempted "2" times overall.
    Password "system\x00" was attempted 2 times.
User account "ubnt" has been attempted "2" times overall.
    Password "ubnt" was attempted 2 times.
User account "888888" has been attempted "3" times overall.
    Password "888888" was attempted 3 times.
User account "Administrator" has been attempted "3" times overall.
    Password "admin" was attempted 3 times.
User account "mother" has been attempted "4" times overall.
    Password "fucker" was attempted 4 times.
User account "guest" has been attempted "5" times overall.
    Password "guest" was attempted 2 times.
    Password "12345" was attempted 3 times.
User account "666666" has been attempted "5" times overall.
    Password "666666" was attempted 5 times.
User account "admin1" has been attempted "5" times overall.
    Password "password" was attempted 5 times.
User account "tech" has been attempted "6" times overall.
    Password "tech" was attempted 6 times.
User account "user" has been attempted "6" times overall.
    Password "user" was attempted 6 times.
User account "support" has been attempted "18" times overall.
    Password "support" was attempted 18 times.
User account "admin" has been attempted "77" times overall.
    Password "Tiverton" was attempted 1 times.
    Password "123456" was attempted 2 times.
    Password "4321" was attempted 2 times.
    Password "7ujMko0admin" was attempted 2 times.
    Password "meinsm" was attempted 2 times.
    Password "1111" was attempted 3 times.
    Password "1111111" was attempted 3 times.
    Password "1234" was attempted 3 times.
    Password "" was attempted 4 times.
    Password "admin1234" was attempted 4 times.
    Password "pass" was attempted 4 times.
    Password "root" was attempted 4 times.
    Password "password" was attempted 6 times.
    Password "smcadmin" was attempted 11 times.
    Password "admin" was attempted 26 times.
User account "root" has been attempted "200" times overall.
    Password "klv1234" was attempted 1 times.
    Password "00000000" was attempted 2 times.
    Password "1234" was attempted 2 times.
    Password "7ujMko0admin" was attempted 2 times.
    Password "default" was attempted 2 times.
    Password "hi3518" was attempted 2 times.
    Password "hunt5759" was attempted 2 times.
    Password "jvbzd" was attempted 2 times.
    Password "klv123" was attempted 2 times.
    Password "pass" was attempted 2 times.
    Password "password" was attempted 2 times.
    Password "realtek" was attempted 2 times.
    Password "tl789" was attempted 2 times.
    Password "zlxx." was attempted 2 times.
    Password "dreambox" was attempted 3 times.
    Password "ikwb" was attempted 3 times.
    Password "ys123456" was attempted 3 times.
    Password "666666" was attempted 4 times.
    Password "7ujMko0vizxv" was attempted 4 times.
    Password "Zte521" was attempted 5 times.
    Password "system" was attempted 5 times.
    Password "" was attempted 6 times.
    Password "123456" was attempted 7 times.
    Password "anko" was attempted 7 times.
    Password "user" was attempted 7 times.
    Password "xmhdipc" was attempted 7 times.
    Password "1111" was attempted 9 times.
    Password "12345" was attempted 10 times.
    Password "admin" was attempted 10 times.
    Password "54321" was attempted 11 times.
    Password "juantech" was attempted 12 times.
    Password "xc3511" was attempted 12 times.
    Password "888888" was attempted 15 times.
    Password "vizxv" was attempted 15 times.
    Password "root" was attempted 18 times.
```
## Expected SHA1 Hash:

```
99eeec61c0f81caa5db090b64b7334ed51db40c0
```
