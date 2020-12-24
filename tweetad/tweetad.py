import sys, json, requests

response = requests.get('https://pbs.twimg.com/hashflag/config-%s.json' % sys.argv[1])

if len(sys.argv) > 2:
	if ('"'+sys.argv[2].lower()+'"') in response.text.lower():
		quit('promoted')
	quit('not promoted')
with open(sys.argv[1] + '.json', 'w+') as file:
	json.dump(response.json(), file, indent=4)
