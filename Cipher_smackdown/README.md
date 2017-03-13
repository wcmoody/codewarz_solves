# Cipher_smackdown

# Description

<p>During a forensic examination, we recovered what we believe to be configuration files for the "NAMBLA" malware to communicate with its C2 node(s). Previous versions of this malware used plain-text config files but these appear to be encrypted. We have no reason to believe they they changed the formatting of the config, it's just encrypted now. Our intel guys say that the crew responsible for "NAMBLA" tend to just use dictionary words padded out with some sort of standard 'sentence ending' punctuation for their keys (if needed).<br/>
For reference, an older "NAMBLA" configuration file can be found <a href="/static/downloads/nambla.txt">Here</a><br/>
<br/>
Example encrypted file can be found <a href="input_data_1.enc">Here</a></p>

## Sample Input:

```
$ ls /path/to/input_data_1.enc
/path/to/input_data_1.enc
```
## Expected Output:

```
$ ./nambla_destroyer.py /path/to/input_data_1.enc
key: "burnish?"
nodes: 1.2.3.4, 5.6.70.80, 9.10.11.12
ports: 443,8080,9000-9999
btc: 1Ez69SnzzmePmZX3WpEzMKTrcBF2gpNQ55
```
## Expected SHA1 Hash:

```
f180ffb2cb8c5e06bd47b8bab6cc55bcf37ab0ab
```
