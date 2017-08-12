#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import codecs
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) != 3:
	print "usage: ./nounphrase.py [input filename from LongLexTo] [output filename]"
	sys.exit()

# filename = raw_input("input file name: ");
filename = sys.argv[1]
# noun_phrase_dict_filename = raw_input("output file name: ");
noun_phrase_dict_filename = sys.argv[2];
nounphrase = {}
nounphrase_all = []
patterns = []
wordcuts = []
pattern_filename = "patterns.txt"
nounpharse_amount_max = 10000


def print_dict(dict):
	for key, value in dict.iteritems():
		print key, value

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
	csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
	for row in csv_reader:
		yield [unicode(cell, 'utf-8') for cell in row]

def contain(big, small):
	for i in big:
		if i in small:
			return True
	return False

def init_patterns():
	file = open(pattern_filename,'r')
	list = map(str.strip, file.readlines()) 
	for temp in list:
		patterns.append(temp.split(','))

def init_wordcut():
	reader = unicode_csv_reader(open(filename))
	for word, partOfSpeech_unsplit in reader:
		if partOfSpeech_unsplit == 'partOfSpeech_unsplit':
			continue
		partOfSpeechs = partOfSpeech_unsplit.encode('utf-8').split(',')
		wordcuts.append([word,partOfSpeechs])

def print_wordcut():
	for wordcut in wordcuts:
		print wordcut[0],wordcut[1]

def add_dict(latest_word, dict_pattern):
	is_already_add = False
	for key in dict_pattern.keys() :
		if latest_word.strip() == key :
			dict_pattern[latest_word.strip()] += 1
			is_already_add = True

		
	if not is_already_add:
		# print 'add ' + latest_word.strip()
	 	dict_pattern[latest_word.strip()] = 1;

def detect_nounphrase():
	latest_nounphrase = ''
	latest_phrase_length = 0
	nouphrase_count = 0

	for pattern in patterns:
		dict_pattern = {}
		for i in range(0,len(wordcuts)-len(pattern)+1):
			if pattern[0] in wordcuts[i][1]:
				for j in range(0,len(pattern)):
					if (not pattern[j] in wordcuts[i+j][1]):
						latest_nounphrase = ''
						latest_phrase_length = 0
						break
					if(wordcuts[i+j][1] != ['']):
						latest_nounphrase += wordcuts[i+j][0]
						latest_phrase_length += 1

					if j == len(pattern)-1:
						if latest_phrase_length > 1:
							add_dict(latest_nounphrase, dict_pattern)
							nouphrase_count += 1;
							latest_nounphrase = ''
							latest_phrase_length = 0
							break
		nounphrase_all.append(dict_pattern)

def dict_filter():
	for dict_pattern in nounphrase_all:
		for key, value in dict_pattern.iteritems():
			if not key in nounphrase:
				nounphrase[key] = value
			else:
				if value >= nounphrase[key]:
					nounphrase[key] = value

# read nounphrase from output file
def init_nounphrase():
	if os.path.isfile(noun_phrase_dict_filename):
		reader = unicode_csv_reader(open(noun_phrase_dict_filename))
		for word, freq in reader:
			word = word.strip()
			if word == 'word':
				continue;
			elif word in nounphrase.keys():
				nounphrase[word] += int(freq)
			else:
				nounphrase[word] = int(freq)

#it still bug -_-!
# def delete_subNounphrase(dict):
# 	nounphrase_noSubNounphrase = {}
# 	# print 
# 	for phrase, value in dict.iteritems():
# 		# is_already_add = False
# 		status = 'not match'
# 		tmp_phrase = ''
# 		for key in nounphrase_noSubNounphrase.keys():
# 			if key == phrase :
# 				status = 'equal'
# 				tmp_phrase = key
# 				break
# 			if key in phrase and status:
# 				status = 'phrase big'
# 				tmp_phrase = key
# 			elif phrase in key:
# 				status = 'phrase small'
# 				tmp_phrase = key
# 		print phrase
# 		try:
# 			if status == 'equal' or status == 'phrase big':
# 				nounphrase_noSubNounphrase[phrase] += 1
# 			elif status == 'phrase small':
# 				nounphrase_noSubNounphrase[phrase] += 1
# 				nounphrase_noSubNounphrase[tmp_phrase] = nounphrase_noSubNounphrase[phrase]
# 				del nounphrase_noSubNounphrase[phrase]
# 			if status == 'not match':
# 				nounphrase_noSubNounphrase[phrase] = 1
# 		except ValueError:
# 			pass

# 	return nounphrase_noSubNounphrase


def write_dict(list_dict):
	nounpharse_amount = 0
	with open(noun_phrase_dict_filename, 'w') as dict_file:
		max_val = 0
		for key,value in list_dict.iteritems():
			if value > max_val:
				max_val = value;

		dict_file.write("word,frequency\n")
		for count in range(max_val,0,-1):
			for key, value in list_dict.iteritems():
				if value == count:
					nounpharse_amount += 1
					dict_file.write((key+ "," + str(value) + '\n').encode('utf-8'))
				if nounpharse_amount >= nounpharse_amount_max:
					break; 

def write_dict_unsort(list_dict):
	with open(noun_phrase_dict_filename, 'w') as dict_file:
		dict_file.write("word,frequency\n")
		for key, value in list_dict.iteritems():
				dict_file.write((key+ "," + str(value) + '\n').encode('utf-8'))

if __name__ == '__main__':
	init_patterns()
	init_wordcut()
	detect_nounphrase()
	dict_filter()
	# temp_nounphrase = delete_subNounphrase(nounphrase)
	# init_nounphrase()
	write_dict(nounphrase)
	# write_dict(temp_nounphrase)
	# write_dict_unsort()