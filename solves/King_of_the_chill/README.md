# King_of_the_chill

# Description

<p>Scrape username/password combos from the first site and brute force the login for the second site. Your app should take two command line arguments. First being the site to be scraped, second being the site to brute force.<br/><br/>
<em>Considerations:</em>
The username and password will be viewable text.
Site structure on the scraped site may not be the same as the example, be flexible.
Post parameters on the brute force site will be the same as the example.
Return the first user:combo set (it's the only one, anyways)<br/>
<em>Test servers available: <a href="http://webs.codewarz.ninja:10003" target="_new">Scrape me</a> and <a href="http://webs.codewarz.ninja:10004" target="_new">Brute me</a></em>
</p>

## Sample Input:

```
$ ./king_of_the_chili_solve.py http://webs.codewarz.ninja:10003 http://webs.codewarz.ninja:10004
```
## Expected Output:

```
$ ./king_of_the_chili_solve.py http://webs.codewarz.ninja:10003 http://webs.codewarz.ninja:10004
Peggy:ureathra
```
## Expected SHA1 Hash:

```
9abc273f0325430fd7557c5bcce1ce4f83f6ca98
```
