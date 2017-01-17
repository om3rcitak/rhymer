# -*- coding: utf-8 -*-
import requests

######################################################
#|--------------------------------------------------|#
#|													|#
#|		coded by om3rcitak www.omercitak.com		|#
#|													|#
#|--------------------------------------------------|#
######################################################

wordlist = "wordlist_tdk.txt"
chars = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
chars_len = len(chars)
keyword_interval = {0:2, 1:15}

def charToIndex(char):
    return chars.index(char)

def indexToChar(index):
	if chars_len <= index:
		raise ValueError("index is out")
	else:
		return chars[index]

def next(string):
	if len(string) <= keyword_interval[0]-1:
		string.append(indexToChar(0))
	else:
		string[0] = indexToChar((charToIndex(string[0]) + 1) % chars_len)
		if charToIndex(string[0]) is 0:
			return list(string[0]) + next(string[1:])
	return string

def request(keyword):
	post_data = {'kelime': keyword, 'ayn': 'tam', 'gonder': 'ARA', 'kategori': 'verilst'}
	post_url = "http://tdk.gov.tr/index.php?option=com_bts&arama=kelime&guid=TDK.GTS.577a444d547022.40146247"
	r = requests.post(post_url, post_data)
	return r.text

def find(keyword):
	response = request(keyword)
	find = response.find(' sözü bulunamadı.')
	if find > -1:
		return False
	else:
		return True

def main():
	sequence = list()
	f = open(wordlist, 'w')
	while True:
		sequence = next(sequence)
		keyword = ''.join(sequence)
		if len(keyword) > keyword_interval[1]:
			break
		isfind = find(keyword)
		print(keyword)
		print(isfind)
		if isfind == True:
			f.write(keyword)
			f.write('\n')
	f.close()
	print("wordlist finished.")

if __name__ == "__main__":
	main()