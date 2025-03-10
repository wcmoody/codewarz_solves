# Find_the_lucky_wifi

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
Your good friend <a href="https://www.youtube.com/watch?v=KEkrWRHCDQU" target="_blank">Hackerman</a> found a novel technique to exploit linksys routers. He has asked you for your support in sorting through his large WigleWifi dumps and geographically locating these routers. He wants you to only print the mac, ssid, lat, lon, and time seen from each entry. He also wants the entries to be sorted with the newest entries at the top. Finally, he modified his wireless collection asset so that it does not store the columns in any particular order and in doing so it sometimes does not capture time correctly (i.e. it defaults to 1969). You should probably throw those entries out. Finally, he walks away mumbling something about GSM entries providing spurious mac addresses and how they need to be dealt with...
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,LAT,LON,AltitudeMeters,AccuracyMeters,Type
68:7f:74:aa:f2:60,niceoak,[wpa-psk-tkip+ccmp][wpa2-psk-tkip+ccmp][wps],9/9/2012 14:24,1,-89,41.4779536,-74.06291007,114.8,0,wifi
00:1c:10:66:8a:02,dumacwpa,[wpa2-psk-ccmp],12/31/1969 19:00,6,-88,41.5027919,-74.06903607,0,157.556015,wifi
00:18:f8:1a:ec:1f,heidi,[wep],7/13/2012 15:58,11,-87,38.88082368,-77.11487787,139.6,0,wifi
00:1c:10:52:ee:24,linksys,[wpa2-psk-ccmp],8/19/2012 7:07,6,-94,40.78346255,-73.82486502,12.6,0,wifi
00:1c:10:52:ee:24,linksys,[wpa2-psk-ccmp],8/19/2012 7:07,6,-94,40.78346255,-73.82486502,12.6,0,wifi
00:25:9c:db:79:3e,linksys,[wps][wep],7/15/2012 17:26,11,-91,38.87557886,-77.12781661,0,50,wifi
00:0b:6b:21:8f:d3,4170005072,[WPA-PSK-TKIP][WPA2-PSK-TKIP],12/31/1969 19:00,6,-88,38.78822744,-77.06754748,0,35.83554077,wifi
00:25:9c:79:74:d9,overtones,[wpa-psk-tkip],8/5/2012 12:58,6,-92,41.45480822,-74.05777598,93.6,0,wifi
00:18:f8:dc:7e:dc,linksys,,9/5/2012 18:55,6,-86,41.33472227,-74.12409448,159.5,0,wifi
68:7f:74:1c:c1:3f,BANKcard,[wps][wep],8/19/2012 7:07,6,-94,40.78275752,-73.82499755,12.1,0,wifi
00:1e:e5:28:d5:c4,bg-office,[wpa2-psk-ccmp],7/5/2012 18:43,8,-96,38.8572008,-77.11091562,40.9,0,wifi
58:6d:8f:70:ee:cc,igor,[wpa-psk-tkip+ccmp][wpa2-psk-tkip+ccmp][wps],8/26/2012 12:00,11,-92,41.44479713,-74.05631538,101.6,0,wifi
58:6d:8f:70:ee:cc,igor,[wpa-psk-tkip+ccmp][wpa2-psk-tkip+ccmp][wps],8/26/2012 11:00,11,-92,41.44479713,-74.05631538,101.6,0,wifi
_0_0,,UNKNOWN;,6/29/2012 12:43,0,-113,38.89150985,-77.0214379,0,629,gsm
_0_0,,UNKNOWN;,6/29/2012 13:47,0,-89,38.8929894,-77.0288934,0,1909,gsm
68:7f:74:b0:43:3c,servmulticambios,[wpa-psk-tkip+ccmp][wpa2-psk-tkip+ccmp][wps],7/14/2012 14:43,1,-83,38.87347753,-77.10462757,91.2,0,wifi
00:1a:70:7c:b5:c3,***private access***,[wep],7/10/2012 14:16,6,-72,38.87763007,-77.11198623,86.2,0,wifi
68:7f:74:1a:94:f3,vermont,[wpa-psk-tkip+ccmp][wpa2-psk-tkip+ccmp][wps],7/15/2012 11:56,6,-89,38.88015025,-77.10846415,93.9,0,wifi
00:25:9c:ea:5a:aa,pepper,[wpa-psk-tkip][wpa2-psk-ccmp-preauth][wps],9/29/2012 14:06,6,-92,42.03942227,-73.98903565,63.9,0,wifi
c0:c1:c0:22:09:4b,frda,[wpa2-psk-ccmp][wps],6/29/2012 16:36,1,-95,38.88083717,-77.11523295,290.2,0,wifi
c0:c1:c0:22:09:4b,frda,[wpa2-psk-ccmp][wps],6/29/2012 16:37,1,-95,38.88083717,-77.11523295,290.2,0,wifi
00:0b:85:8d:61:3f,arlington ag,[WPA2-PSK-TKIP+CCMP],12/31/1969 19:00,1,-98,38.88082985,-77.11518262,0,39.96046829,wifi
00:24:6c:31:82:c1,Medisys_I,[WPA2-EAP-CCMP],8/19/2012 7:14,7,-90,40.70251545,-73.81648227,19.7,0,WIFI
00:24:6c:31:82:c1,Medisys_I,[WPA2-EAP-CCMP],8/19/2012 7:15,7,-93,40.70099013,-73.81574828,22.5,0,WIFI
```
## Expected Output:

```
$ ./find_the_lucky_wifi_solve.py /path/to/somefile.txt
00:25:9c:ea:5a:aa pepper 42.03942227 -73.98903565 2012/09/29 14:06:00
68:7f:74:aa:f2:60 niceoak 41.4779536 -74.06291007 2012/09/09 14:24:00
00:18:f8:dc:7e:dc linksys 41.33472227 -74.12409448 2012/09/05 18:55:00
58:6d:8f:70:ee:cc igor 41.44479713 -74.05631538 2012/08/26 12:00:00
68:7f:74:1c:c1:3f bankcard 40.78275752 -73.82499755 2012/08/19 07:07:00
00:1c:10:52:ee:24 linksys 40.78346255 -73.82486502 2012/08/19 07:07:00
00:25:9c:79:74:d9 overtones 41.45480822 -74.05777598 2012/08/05 12:58:00
00:25:9c:db:79:3e linksys 38.87557886 -77.12781661 2012/07/15 17:26:00
68:7f:74:1a:94:f3 vermont 38.88015025 -77.10846415 2012/07/15 11:56:00
68:7f:74:b0:43:3c servmulticambios 38.87347753 -77.10462757 2012/07/14 14:43:00
00:18:f8:1a:ec:1f heidi 38.88082368 -77.11487787 2012/07/13 15:58:00
00:1a:70:7c:b5:c3 ***private access*** 38.87763007 -77.11198623 2012/07/10 14:16:00
00:1e:e5:28:d5:c4 bg-office 38.8572008 -77.11091562 2012/07/05 18:43:00
c0:c1:c0:22:09:4b frda 38.88083717 -77.11523295 2012/06/29 16:37:00
```
## Expected SHA1 Hash:

```
539a932e5557151d92178ad2589929e11721bbfd
```
