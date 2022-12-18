import sys
import requests

tests = [
	"?callback=x&cb=x&jsonp=x&jsonpcallback=x&jsonpcb=x&jsonp_cb=x&json=x&jsoncallback=x&jcb=x&call=x&cb_=x&_cb_=x",
	".jsonp?callback=x&cb=x&jsonp=x&jsonpcallback=x&jsonpcb=x&jsonp_cb=x&json=x&jsoncallback=x&jcb=x&call=x&cb_=x&_cb_=x",
]

def check(url):
	for test in tests:
		try:
			response = requests.get(url + test)
			if response.text.startswith('x('):
				print("VULN:", response.url)
		except Exception as e:
			print(e, file=sys.stderr)

if not sys.stdin.isatty():
	for line in sys.stdin:
		check(line)
else:
	print("Usage: cat urls.txt | python3 main.py", file=sys.stderr)
