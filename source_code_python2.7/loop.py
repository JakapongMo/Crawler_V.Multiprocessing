#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import csv
from bs4 import BeautifulSoup
from string import whitespace


file_path = '/home/tengmo/crawler_to_server_set_time/crawler/store/4000filter.arc'
dict_site = eval(open("/home/tengmo/crawler_to_server_set_time/crawler/result/dict_site.txt").read())

block = 0
cnt = 1
f = open(file_path, "r")
lineList = f.readlines()
'''
if len(line) > 7:
    if str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
'''

first = len(lineList)/4
second = 2*(len(lineList)/4)
third = 3*(len(lineList)/4)
line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
print first
print second
print third
check = "first"
for line in lineList:
    if cnt <= first and len(line) > 7 and str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
        check = "first"
    elif cnt <= second and len(line) > 7 and str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
        check = "second"
    elif cnt <= third and len(line) > 7 and str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
        check = "third"
    elif cnt > third and len(line) > 7 and str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
        check = "four"
    cnt+=1

    if check == "first":
        line_1 += line
    elif check == "second":
        line_2 += line
    elif check == "third":
        line_3 += line
    elif check == "four":
        line_4 += line
print line_4


with open('/home/tengmo/crawler_to_server_set_time/crawler/result/sub1.txt' , 'w') as out:
    out.write(line_1)
with open('/home/tengmo/crawler_to_server_set_time/crawler/result/sub2.txt' , 'w') as out:
    out.write(line_2)
with open('/home/tengmo/crawler_to_server_set_time/crawler/result/sub3.txt' , 'w') as out:
    out.write(line_3)
with open('/home/tengmo/crawler_to_server_set_time/crawler/result/sub4.txt' , 'w') as out:
    out.write(line_4)
