import sys
import requests

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept": "text/javascript, text/html, application/xml, text/xml, */*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"X-Requested-With": "XMLHttpRequest",
"X-Prototype-Version": "1.6.0",
"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"Content-Length": "33",
"Origin": "https://www.yougetsignal.com",
"Connection": "keep-alive",
"Referer": "https://www.yougetsignal.com/",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-site",
"TE": "trailers"}

payload = {"remoteAddress": sys.argv[1], "key": ""}
data = requests.post("https://domains.yougetsignal.com/domains.php", data=payload, headers=headers).json()
for each in data["domainArray"]:
	print(each[0])
