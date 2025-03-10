# Dream_slice

# Description

<p>Can you recognize the pattern of the manipulated text and correct it?
<br/>
<strong>Note:</strong> You don't have to worry about words 8 chars or over. And do you see a pattern of how the word order was changed per line?</p>

## Sample Input:

```
$ cat samplefile
inaag vOre nad vore
omemtn I erilev hte
iwhtni I ma ngbeiar hte ubdrne
ksni pOne ownusd ihddne erdun ym

lbeesd aPni si erla sa a uct htta
epesl hTe afec I ese ryeev item I rty ot
rciygn ngStiar ta em
```
## Expected Output:

```
$ ./solve.py /path/to/samplefile
Over and over again
I relive the moment
I am bearing the burden within
Open wounds hidden under my skin

Pain is real as a cut that bleeds
The face I see every time I try to sleep
Staring at me crying
```
## Expected SHA1 Hash:

```
89ec48c2979455fa6494504df28ea440e898c3c2
```
