# Chattribution

# Description

<p>We need to attribute some usernames to their IP address from this rogue chat server we located. Carve them out of the PCAP so we can add this info to our forensic stuffs.<br/>
<em>Example pcap <a href="chat_1.pcap">here</a></em>
</p>

## Sample Input:

```
$ chattribution_solve.php /path/to/somefile.pcap
```
## Expected Output:

```
$ chattribution_solve.php /path/to/somefile.pcap
10.0.100.65 =&gt; server
10.0.100.76 =&gt; unknown
10.0.100.82 =&gt; ohai
10.0.100.90 =&gt; billy
10.0.100.91 =&gt; raejae
```
## Expected SHA1 Hash:

```
9b59d1a11b3b318d2300fbfcbb02b0b1b101c1bc
```
