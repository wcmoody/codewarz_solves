import os
import re
import requests
import time
from bs4 import BeautifulSoup as bs

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://codewarz.ninja/'

solves = os.listdir('solves')

s = requests.Session()

username = "madeye"
password = "eeTY55lU2W2i"

r = s.get(url, verify=False)
cookies = r.cookies
r = s.get(url+'login', cookies=cookies)
soup = bs(r.text, "html5lib")
inputs = [(element['name'],element['value']) for element \
        in soup.find_all("input", type="hidden") ]

payload = {}
for i,v in inputs:
    payload[i] = v

payload['username'] = username
payload['password'] = password
h = {"Referer":"https://codewarz.ninja/login", 
        "Content-Type": "application/x-www-form-urlencoded"}

r = s.post(url+'/login', headers = h, data=payload, cookies=cookies, verify=False)
r = s.get(url+'challenges', verify=False)


soup = bs(r.text,"html5lib")
challenges = []
for a in soup.find_all('a', href=True):
    if "do_challenge" in a['href']:
        challenges.append(a['href'])

headings = ["Sample Input:", "Expected Output:", "Expected SHA1 Hash:"]


# the block below has not been confirmed on current version
# this is because, well i don't have any challenges to submit solve for
for challenge in challenges:
    solvecode = challenge.split('/')[2] + '.py'
    r = s.get(url+challenge)
    challsoup = bs(r.text, "html5lib")
    pres = challsoup.find_all("pre")
    desc = str(challsoup.p)
    name = challenge.split("/")[2]

    """
    # build the readme files
    with open("../" + name + "/" + "README.md", "w") as f:
        f.write("# " + name + "\n\n")
        f.write("# Description\n\n")
        f.write(str(desc) + "\n\n")
        for head, pre in zip(headings,pres[-3:]):
            trim_pre = str(pre)[5:-6]
            f.write("## %s\n\n" % head)
            f.write("```\n%s\n```\n" % trim_pre)
    """
    # Build the input files
    if len(str(pres[-3]).split("\n")) > 1:
        with open ("../%s/%s_input.txt" % (name,name), "w") as f:
            print "%s has input file" % name
            for line in str(pres[-3]).split("\n")[1:]:
                f.write(line.strip("</pre>") + "\n")

   
    #update_readme = []
    ## Download the extra files

    #linkpatt = re.compile("""(<a href="([^"]*?)">(.*)</a>)""")
    #matches = linkpatt.findall(desc)
    #for m in matches:
    #    if not m[1].startswith("/static"): continue
    #    link = m[1]
    #    print "Downloading", link, "for\t", name
    #    """
    #    r = requests.get("https://codewarz.ninja" + link, stream=True)
    #    with open("../%s/%s" % (name, link.split("/")[-1]), "w") as f:
	#		for chunk in r.iter_content(chunk_size=1024): 
	#			if chunk: 
	#				f.write(chunk)
    #    """
    #    update_readme.append((name,m))

    #for update,match in update_readme:
    #    old_link = m[0]
    #    link = m[1]
    #    hypertext = m[2]
    #    with open("../%s/README.md" % name) as f:
    #        readme = f.read()
    #    readme = readme.replace(link,link.split("/")[-1])
    #    with open("../%s/README.md" % name, "w") as f:
    #        f.write(readme)
    #""" 


    #"""
    ## upload the solve code
    #inputs = [(element['name'],element['value']) for element \
    #        in challsoup.find_all('input') if element['type'] == 'hidden' ]
    #payload = {}
    #payload['submit'] = 'submit'
    #for i, v in inputs:
    #    payload[i] = v
    #src = [('code',(solvecode, open('solves/'+solvecode,'r'),'text/x-script.python'))]
    #s.headers.update({'referer':'https://codewarz.ninja/challenges'}) 
    #r = s.post(url+challenge,data=payload,files=src)
    #print r.status_code
    #"""







#with open('test.html','w') as output:
#    output.write(r.text)



