# Pop_a_pcap

# Description

<p>Ze Germans have been brute forcing our users passwords. We are too incompetent to figure out how to mitigate the attack so we will just tell whatever user who had a dumb password that he needs to change it. Parse the pcap and print out the username of the victim and whatever secret information was stolen (hint: it's the flag).<br/>
<em>Example pcap <a href="/static/downloads/z_comp_bruted.pcap">Here</a></em>
</p>

## Sample Input:

```
$ ./pop_a_pcap_solve.py /path/to/z_comp_bruted.pcap
```
## Expected Output:

```
$ ./pop_a_pcap_solve.py /path/to/z_comp_bruted.pcap
bob CTD{This_is_not_THE-real_flag_bravosierra99}
```
## Expected SHA1 Hash:

```
357f97818e6db1c48fdfe0dc970396c7ec4a8297
```
