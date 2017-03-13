# Apache_it_all_night_long

# Description

<p>As if the original challenge apache_log_parser wasn't bad enough, now this guy only wants to see what web browser user agents that are hitting his website. There has also been a change to the ordering from most hits instead of first, now they are last. Lastly the histogram is slightly different? Can you write a program to mimic the output? Be mindful that the length of the justify has to grow with the largest amount of stars. IE: if you have 10 stars you need to justify for 10 spaces, or if you have 30 stars, you need to justify for 30 spaces.
<br/><br/><a href="/static/downloads/Apache_it_all_night_long_input1.log">Download the sample data file here</a></p>

## Sample Input:

```
$ ./apache_it_all_night_long_solve.py /path/to/Apache_it_all_night_long_input1.log
```
## Expected Output:

```
$ ./apache_it_all_night_long_solve.py /path/to/somefile.txt
           *: 1 "Mozilla/4.0 (compatible) Wormly SSL Tester"
           *: 1 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; InfoPath.2)"
           *: 1 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko)"
           *: 1 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17"
           *: 1 "Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/31.0"
           *: 1 "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
           *: 1 "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4"
           *: 1 "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7"
           *: 1 "Mozilla/5.0 zgrab/0.x"
           *: 1 "Site Check (Experimental)"
           *: 1 "Validator.nu/LV http://validator.w3.org/services"
           *: 1 "Wget/1.16 (linux-gnu)"
           *: 1 "libwww-perl"
           *: 2 "CSS Certificate Spider (http://www.css-security.com/certificatespider/)"
           *: 2 "Googlebot/2.1; +http://www.google.com/bot.html)"
           *: 2 "Mozilla/4.0 (compatible; Synapse)"
           *: 2 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25"
           *: 2 "Mozilla/5.0 (Windows NT 6.3; rv:36.0 Gecko/20100101 Firefox/36.0"
           *: 2 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8"
           *: 2 "Mozilla/5.0 (compatible; DomainSONOCrawler/0.1; +http://domainsono.com)"
           *: 2 "Mozilla/5.0 (compatible; MSIE 8.0; MSIE 9.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)"
           *: 2 "Mozilla/5.0 (compatible; MSIE 9.0; Windows) AppEngine-Google; (+http://code.google.com/appengine; appid: s~unmask-parasites2)"
           *: 2 "Mozilla/5.0"
           *: 2 "Ruby"
           *: 2 "python-requests/2.2.1 CPython/2.7.6 Linux/3.13.0-57-generic"
           *: 3 "Google favicon"
           *: 3 "Java/1.8.0_51"
           *: 3 "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Qt/4.7.1 Safari/533.3"
           *: 3 "Mozilla/5.0 (compatible; Google-Site-Verification/1.0)"
           *: 3 "Python-urllib/2.7"
           *: 3 "SSL Labs (https://www.ssllabs.com/about/assessment.html)"
           *: 3 "W3C_Validator/1.3 http://validator.w3.org/services"
           *: 3 "python-requests/2.8.0"
           *: 4 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; PTST 2.295)"
           *: 4 "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +http://www.cloudflare.com/always-online)"
           *: 4 "Mozilla/5.0 (compatible; Scrubby/3.1; +http://www.scrubtheweb.com/help/technology.html)"
           *: 5 "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0"
           *: 5 "W3C_Validator/1.2"
           *: 6 "Mozilla/5.0 (Windows NT 5.1) BrokenLinkCheck.com/1.1"
           *: 6 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)"
           *: 6 "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
           *: 11 "Safari/11601.2.7.2 CFNetwork/760.1.2 Darwin/15.0.0 (x86_64)"
           *: 17 "RankFlex.com Webspider"
           *: 21 "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
           *: 25 "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"
           *: 26 "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
           *: 26 "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"
           *: 26 "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
           *: 36 "Googlebot/2.1 (+http://www.google.com/bot.html)"
           *: 36 "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0) CrawlerProcess (http://www.PowerMapper.com) /5.10.736.0"
          **: 50 "Apache/2.4.7 (Ubuntu) PHP/5.5.9-1ubuntu4.14 (internal dummy connection)"
          **: 81 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7"
         ***: 115 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
         ***: 123 "W3C-mobileOK/DDC-1.0 (see http://www.w3.org/2006/07/mobileok-ddc)"
        ****: 161 "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +http://www.cloudflare.com/always-online) AppleWebKit/534.34"
        ****: 191 "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 wootwoot/38.4.0"
       *****: 209 "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Whatwhat/38.3.0"
     *******: 314 "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Really/38.4.0"
     *******: 330 "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    ********: 385 "Apache/2.4.7 (Ubuntu) PHP/5.5.9-1ubuntu4.14 OpenSSL/1.0.1f (internal dummy connection)"
   *********: 444 "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.4.0"
  **********: 494 "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Whatwhat/38.4.0"
************: 576 "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 holycrap/38.4.0"
```
## Expected SHA1 Hash:

```
e898a504fbc729af3418c20e8a91006deab78381
```
