# -*- coding: utf-8 -*-
import argparse

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

DEFAULT_WORD_LIST = "wordlist_tdk.txt"
MAX_DESTINATION = 1
DESCRIPTION = 'rhymer, find the nearest word is a word using levenshtein algorithm helps make the rhyme songwriter.'

parser = argparse.ArgumentParser('rhymer', description=DESCRIPTION)
parser.add_argument('-k', '--keyword', type=str, required=True)
parser.add_argument('-w', '--wordlist', default=DEFAULT_WORD_LIST)
args = parser.parse_args()


def levenshtein(string1, string2):
    """
	:param string1:
    :param string2:
    :return:
    """
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


def main():
    keyword = args.keyword
    with open(args.wordlist, 'r') as file:
        for line in file:
            destination = levenshtein(keyword, line.rstrip())
            if destination <= MAX_DESTINATION:
                print(line.rstrip())


if __name__ == "__main__":
    main()
