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

arg = sys.argv[1]
path_dir = sys.argv[2]


file_path = '/home/tengmo/crawler_to_server_set_time/crawler/store/%s.arc'%arg
dict_site = eval(open("{0}/dict_site_{1}.txt".format(path_dir, arg)).read())
if (os.path.exists('{0}/sub1_{1}.txt'.format(path_dir,arg))):
    print "sub1_%s already exists"%arg
    sys.exit()



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
#print line_4

'''
with open('{0}/sub1_{1}.txt'.format(path_dir,arg) , 'w') as out1:
    out1.write(line_1)
with open('{0}/sub2_{1}.txt'.format(path_dir,arg) , 'w') as out2:
    out2.write(line_2)
with open('{0}/sub3_{1}.txt'.format(path_dir,arg) , 'w') as out3:
    out3.write(line_3)
with open('{0}/sub4_{1}.txt'.format(path_dir,arg) , 'w') as out4:
    out4.write(line_4)
'''
out1 = open('{0}/sub1_{1}.txt'.format(path_dir,arg), "w")
out1.write(line_1)
out1.close()
out2 = open('{0}/sub2_{1}.txt'.format(path_dir,arg), "w")
out2.write(line_2)
out2.close()
out3 = open('{0}/sub3_{1}.txt'.format(path_dir,arg), "w")
out3.write(line_3)
out3.close()
out4 = open('{0}/sub4_{1}.txt'.format(path_dir,arg), "w")
out4.write(line_4)
out4.close()


sys.exit(0)
