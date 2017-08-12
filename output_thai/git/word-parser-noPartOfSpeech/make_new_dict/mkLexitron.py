#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
from mkDict import read_type_file
reload(sys)
sys.setdefaultencoding('UTF8')

print('START MAKING LEXITRON...\n')
print('DELETE TYPE: "example sentence"...')
abbreviation = read_type_file('thai_dict/types.txt')

in_file_str = 'thai_dict/dict.txt'
out_file_str1 = 'thai_dict/lexitron.txt'
out_file_str2 = 'thai_dict/lexitron_without_type.txt'
in_file = open(in_file_str,'r')
out_file1 = open(out_file_str1,'w')
out_file2 = open(out_file_str2,'w')
line = in_file.readline()
while len(line) > 0:

	split_line = line.split('|')
	word = split_line[0]
	abv = split_line[1]
	if len(abv) > 0 :
		#abvs = abv.split(',')
		#if not 'example sentence' in abv:
		#out_file1.write(cut_last_char(word,' ') + '|' + abv +'\n')
		#out_file2.write(cut_last_char(word,' ') + '\n')
		out_file1.write(word.strip('\u00A0') + '|' + abv)
		out_file2.write(word.strip('\u00A0'))
	line = in_file.readline()

print('FINISHED MAKE LEXITRON(lexitron.txt) (lexitron_without_type.txt)\n\n')

print('********************\n\n      THANK YOU      \n\n********************')