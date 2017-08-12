import sys
import os.path
import json
import csv
from urllib import urlopen

reload(sys)
sys.setdefaultencoding('UTF8')

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

def add_json(out_file,json_file):
	json_data = json.loads(json_file)
	#json_data = open(json_file).read()
	out_file.write(str(json_data) + '\n')

room_col = 0
start_col = 1
stop_col = 2
first_topic = 3
head = '</body>\n</html>'
tail = '<html>\n<body>\n'
head_length = len(head)
tail_length = len(tail)
out_file_str = 'result.txt'
out_file = open(out_file_str,'w')
with open('pt_updatelog/updateLog_00_00') as f:
	rows = csv.reader(f)
	for r in rows:
		for i in range(first_topic,len(r)):
			topic_id = cut_first_char(cut_last_char(r[i],']'),' ')
			url = 'https://earth.mikelab.net:55443/topic.php?topic=' + str(topic_id)
			raw_html = urlopen(url).read()
			raw_html = raw_html[head_length:len(raw_html) - tail_length - 2]
			add_json(out_file,raw_html)
