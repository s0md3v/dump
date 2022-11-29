import re
import sys
import requests

domain_pattern = r"</td></tr><tr><td>([^<]+)"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "deflate",
"DNT": "1",
"Connection": "keep-alive",
"Referer": "https://viewdns.info/reversewhois/?q=Nokia+Inc.",
"Cookie": "PHPSESSID=n67oo2oocm6or5ldi990o7ufb6",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1"}

response = requests.get("https://viewdns.info/reversewhois/?q=" + sys.argv[1], headers=headers).text
for domain in re.findall(domain_pattern, response):
	print(domain)
