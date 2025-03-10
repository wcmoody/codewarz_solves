# Cyber_haiku_dictionary

# Description

<p>Someone dropped our cyber haiku dictionary and the order in which they were stored is all messed up. Can you fix the order dictionary and print them out in the right order?</p>

## Sample Input:

```
$ cat samplefile
{'24': 'Wordpress', '25': 'instance', '26': 'is', '27': 'completely', '20': 'by', '21': 'default', '22': '\n', '23': 'My', '28': 'secure', '29': '\n', '1': "We're", '3': '-', '2': 'good', '5': 'used', '4': 'we', '7': 'encryption.', '6': 'strong', '9': "You're", '8': '\n', '11': 'talking', '10': 'just', '13': 'theoretical', '12': 'about', '15': '\n', '14': 'concerns.', '17': 'TLS', '16': 'Yes,', '19': 'enabled', '18': 'is', '31': 'Masters', '30': 'InfoSec', '36': '\n', '35': 'botnet?"', '34': 'a', '33': '"What\'s', '32': 'degree:'}
```
## Expected Output:

```
$ ./solve.py /path/to/samplefile
We're good - we used strong encryption.
You're just talking about theoretical concerns.
Yes, TLS is enabled by default
My Wordpress instance is completely secure
InfoSec Masters degree: "What's a botnet?"
```
## Expected SHA1 Hash:

```
d1a1bcbf5dee042a6abf3f42c604c0f3113342ac
```
