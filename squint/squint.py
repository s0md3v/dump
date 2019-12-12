import enchant
import itertools

spellChecker = enchant.Dict('en')

characters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-')

upper = ('b', 'd', 'f', 'h', 'i', 'j', 'k', 'l', 't')
lower = ('g', 'j', 'p', 'q', 'y')
hole = ('a', 'b', 'e', 'g', 'o', 'p', 'q')

string = {
	0 : {
		'minLength' : 5,
		'maxLength' : 5,
		'indexes' : {
				0 : ('v'),
				1 : ('o'),
				-1 : lower
		 }
	},
}

allPossibleWords = []

for word, conditions in string.items():
	possibleWords = set()
	for name in range(conditions['minLength'], conditions['maxLength'] + 1):
		with open('/root/squint/db/%i.txt' % name) as f:
			for line in f:
				allFine = True
				word = line.rstrip('\n')
				for i in conditions['indexes']:
					try:
						if not word[i] in conditions['indexes'][i]:
							allFine = False
							continue
					except IndexError:
						print (word)
				if allFine and spellChecker.check(word):
						possibleWords.add(word)
	allPossibleWords.append(possibleWords)

for first in allPossibleWords[0]:
	string = first
	print (string)