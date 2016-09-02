# -*- coding: utf-8 -*-
import sys, argparse

'''                             
      | |                                          
  _ __| |__  _   _ _ __ ___   ___ _ __ _ __  _   _ 
 | '__| '_ \| | | | '_ ` _ \ / _ \ '__| '_ \| | | |
 | |  | | | | |_| | | | | | |  __/ |_ | |_) | |_| |
 |_|  |_| |_|\__, |_| |_| |_|\___|_(_)| .__/ \__, |
              __/ |                   | |     __/ |
             |___/                    |_|    |___/
			 
			 
		coded by Om3rCitak - www.omercitak.com
'''

wordlist = "wordlist_tdk.txt"
max_dest = 1

def usage():
	print('usage: rhymer.py [-h] [-k KEYWORD]\n')
	print('optional arguments:')
	print('  -h, --help            show this help message and exit')
	print('  -k KEYWORD, --keyword KEYWORD')

def levenshtein(string1, string2):

	if len(string1) < len(string2):
		return levenshtein(string2, string1)

	if len(string2) == 0:
		return len(string1)

	previous = range(len(string2) + 1)

	for i, current1 in enumerate(string1):
		current = [i + 1]
		for j, current2 in enumerate(string2):
			insertions = previous[j + 1] + 1
			deletions = current[j] + 1
			substitutions = previous[j] + (current1 != current2)
			current.append(min(insertions, deletions, substitutions))
		previous = current

	return previous[-1]

def main(argv):

	parser = argparse.ArgumentParser()
	parser.add_argument('-k', '--keyword')
	args = parser.parse_args()
	keyword = args.keyword
	
	if keyword == None:
		usage()
		sys.exit(0)

	file = open(wordlist)

	for line in file:
		dest = levenshtein(keyword, line.rstrip())
		if dest <= max_dest:
			print(line.rstrip())

	file.close()

if __name__ == "__main__":
	main(sys.argv[1:])