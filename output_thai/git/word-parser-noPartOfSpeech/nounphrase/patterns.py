#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import codecs
import sys
filename = "patterns.txt"



def write_pattern(list_pattern):
	with open(filename, 'a') as file:
		# dict_file.write("word,frequency\n")
		# for key, value in list_dict.iteritems():
		# 		dict_file.write((key+ "," + str(value) + '\n').encode('utf-8'))
		for ele in list_pattern:
			file.write(ele + ",")
		file.write('\n')

if __name__ == '__main__':
	n = 20;
	list_pattern = [];
	for i in range(1,n+1):
		for j in range(0,i+1):
			list_pattern.append("noun")
		print list_pattern #only noun
		write_pattern(list_pattern)

		adjective_list = list_pattern
		adjective_list[len(adjective_list)-1] = "adjective"
		write_pattern(adjective_list)
		print adjective_list

		adjective_list.append("adverb");
		write_pattern(adjective_list)
		print adjective_list

		list_pattern = []