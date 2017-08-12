#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path

reload(sys)
sys.setdefaultencoding('UTF8')
abbreviation = ['noun','example sentence','verb','phrase','classifier','conjunction','particle','adverb','adjective','prefix','proper noun']

def add_to_abbreviation(abbreviation,now_abv):
	for abv in now_abv:
		if not abv in abbreviation:
			abbreviation.append(abv)
	return abbreviation

def write_abv(out_file,now_abv):
	out_file.write('|')
	count = 0
	for abv in now_abv:
		if count == 0:
			out_file.write(abv)
		else:
			out_file.write(','+abv)
		count += 1

def add_to_abv(now_abv,s,start_at):
	abv = s[start_at][1:]
	if not abv in now_abv:
		now_abv.append(abv)
	i = start_at+1
	while s[i][len(s[i])-1] != '"':
		abv = s[i][1:]
		if not abv in now_abv:
			now_abv.append(s[i][1:])
		i += 1

	abv = s[i][1:len(s[i])-1]
	if not abv in now_abv:
		now_abv.append(abv)
	return now_abv

def cut_character(string,character):
	#word|abbreviation
	i=0
	cut_str = ""
	while i < len(string):
		if string[i] != character:
			cut_str += string[i]
		i += 1
	return cut_str

def make_new_dict(number,abbreviation):
	in_file_str = "dict/"+str(number)+".csv"
	#out_file_str = "dict/"+str(number)+".txt"
	out_file_str = "dict/lexitron.txt"
	row_count = 0
	if os.path.exists(in_file_str):
		in_file = open(in_file_str,'r')
		#out_file = open(out_file_str,'w')
		out_file = open(out_file_str,'a')
		line = in_file.readline()
		line = in_file.readline()
		line = in_file.readline()
		row_count = 3
		now_abv = []
		now_word = ""
		while(len(line) != 0):
			s = line.split(',')
			#print(s)
			if len(s) > 3 :
				if len(s[0]) > 0 :
					word = cut_character(s[0],'"')
					if not word in abbreviation:
						if row_count > 3:
							#if 'example sentence' in now_abv:
							write_abv(out_file,now_abv)
							out_file.write('\n')
							abbreviation = add_to_abbreviation(abbreviation,now_abv)
							now_abv = []
						out_file.write(s[0])
						row_count += 1
				
						if len(s[2]) > 0:
							if s[2][0] != '"':
								if not s[2] in now_abv:
									now_abv.append(s[2])
							else:
								now_abv = add_to_abv(now_abv,s,2)
					else:
						if s[0][0] != '"': 
							if not s[0] in now_abv:
								now_abv.append(s[0])
						else:
							now_abv = add_to_abv(now_abv,s,0)

			line = in_file.readline()

		out_file.close()
		in_file.close()
		print(abbreviation)

for num in range(161,207):
	make_new_dict(num,abbreviation)