#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import csv

reload(sys)
sys.setdefaultencoding('UTF8')

def read_type_file(types_file_str):
	types = []
	types_file = open(types_file_str,'r')
	line = types_file.readline()
	while len(line) > 0 :
		line = cut_last_char(line,'\n')         
		if len(line) > 0 :
			types.append(line)
		line = types_file.readline()
	types_file.close()
	return types 

def write_type_file(types_file_str,types):
	types.sort()
	types_file = open(types_file_str,'w')
	for now_type in types:
		types_file.write(cut_first_char(now_type,' ') + '\n')
	types_file.close()


def add_type(now_type,string) :
	string_split = string.split(',')
	for this_type in string_split:
		if not this_type in now_type and len(this_type) > 0 :
			now_type.append(cut_first_char(this_type,' '))
	return now_type

def cut_first_char(string,char):
	if len(string) >= len(char):
		if string[:len(char)] == char:
			return string[len(char):]
	return string

def cut_last_char(string,char):
	if len(string) >= len(char):
		if string[len(string)-len(char):] == char:
			return string[:len(string)-len(char)]
	return string

def cut_string(string,character) :
	out_string = ""
	for char in string :
		if char != character :
			out_string+=char
	return out_string


def write_type(out_file,now_type) :
	length = len(now_type)
	out_file.write('|')
	for num in range(0,length) :
		if num > 0:
			out_file.write(',')
		out_file.write(now_type[num])
	out_file.write('\n')
	return []

def write_word(out_file,word):
	word = word.replace(u'\u00A0','')
	word = word.strip(u'\u00A0')
	word = word.replace(u'\u0020','')
	word = cut_first_char(word,' ')
	word = cut_last_char(word,' ')
	out_file.write(word)

def add_dict_type(types,now_type) :
	for type in now_type:
		if not type in types:
			types.append(cut_first_char(cut_first_char(type,' '),' '))
	return types

def make_file(types,num,out_file_str) :
	word_col = 0
	type_col = 2
	meaning_col = 3
	now_type = []
	num_row = 1
	in_file_str = 'thai_dict/' + str(num) +'.csv'
	if os.path.exists(in_file_str) :
		out_file = open(out_file_str,'a')
		with open(in_file_str) as f :
			rows = csv.reader(f)
			for r in rows:
				if len(r[word_col]) != 0 and len(r[meaning_col]) != 0 :
					if r[word_col] != 'abbreviation' and r[type_col] != 'abbreviation' and r[type_col] != 'type':
						if num_row > 1 :
							types = add_dict_type(types,now_type)
							now_type = write_type(out_file,now_type)
						write_word(out_file,r[word_col].strip())
						now_type = add_type(now_type,r[type_col])
						num_row += 1
				elif r[word_col].split(',')[0] in types:
						now_type = add_type(now_type,r[word_col])
		now_type = write_type(out_file,now_type)
		out_file.close()
	return types

def clear_file(out_file_str) :
	out_file = open(out_file_str,'w')
	out_file.close()

print('START MAKING DICTIONARY...\n')
types_file_str = 'thai_dict/types.txt'
types = read_type_file(types_file_str)
out_file_str = 'thai_dict/dict.txt'
clear_file(out_file_str)
for num in range(161,207):
	types = make_file(types,num,out_file_str)
print('FINISHED MAKE DICTIONARY(dict.txt)\n')
print('TYPES:')
print(types)
write_type_file(types_file_str,types)
print('\nFINISHED UPDATE TYPES(types.txt)\n')