#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import csv
import json
from bs4 import BeautifulSoup
from string import whitespace


file_path = '/home/tengmo/crawler_to_server_set_time/crawler/result/sub2.txt'
dict_site = eval(open("/home/tengmo/crawler_to_server_set_time/crawler/result/dict_site.txt").read())

HAVE_TITLE = 0
NO_TITLE = 0
TH = 0
ENG = 0
OTHER = 0
NO_CONTENT =0
No_page = 0

text_html = 0
text_plain = 0
text_Not_itdentified = 0
text_other = 0
start_time = time.time()
json_dict = {}


############################################################################################
def Use(line_1, line_2, line_3, line_4, line_5, line_6, html_content):
    print line_1
    #print line_2
    print line_3
    #print line_4
    #print line_5
    #print line_6
    print html_content

############################################################################################

def Find_title_def(html_content):
    global HAVE_TITLE
    global NO_TITLE
    soup = BeautifulSoup(html_content, 'lxml', from_encoding="utf-8")

    #return soup.title

    try:
        if (soup.title.string) == None:
            NO_TITLE += 1
            return "No_title"

        else:
            HAVE_TITLE += 1
            return (soup.title.string)
    except AttributeError:
        NO_TITLE +=1
        return ("No_title")

############################################################################################

def Find_binary_domain(URL):
    Domain_name = ''
    for char in URL[7:]:
        if(char == '/'):
            break
        Domain_name += char
    #print(Domain_name)

    list_string = ['.com', '.edu', '.gov', '.org', '.net', '.mil', '.co.th', '.in.th', '.ac.th']
    list_domain = [0,0,0,0,0,0,0,0,0,0]
    for x in range(0,9):
        if(find_str(Domain_name, list_string[x])):
            list_domain[x] += 1
    count = 0
    for x in range(0,9):
        if(list_domain[x] == 0):
            count +=1
    if count == 9:
        list_domain[9] +=1

    string =''
    for x in list_domain:
        string += str(x)
    return string

#    com = 0
#    edu = 0
#    gov = 0
#    org = 0
#    net = 0
#    mil = 0
#    co_th = 0
#    in_th = 0
#    ac_th = 0
#    other = 0

################################################################################

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return True

            index += 1

    return False

################################################################################
def Find_URL_NB_Slash_LenURL(line_1):
    #print (INPUT_URL)
    URL = ''
    Nb_slash = 0
    before = ''
    for char in line_1:
        if char == '/':
            Nb_slash +=1
        if char  == ' ':
            break
        URL += char

    Nb_slash = Nb_slash - 2
    cnt = 0
    check = False
    for char in URL:
        cnt+=1
        if cnt > len(URL) -6:
            if char == '.':
                check = True
    if Nb_slash >0 and check:
        Nb_slash -=1
    if URL[len(URL)-1] == "/" and Nb_slash > 0:
        Nb_slash -= 1

    yield URL
    yield Nb_slash
    yield len(URL)- 7 - Nb_slash

################################################################################

def Find_site(line_1):
    site = ''
    Nb_point =0
    Nb_slash =0
    cnt = 0
    index =0
    for word in line_1.split():
        index+=1
        if index == 1:

            cnt =0
            for char in word:
                cnt +=1
                if char == '.':
                    Nb_point +=1
                if char == '/':
                    Nb_slash +=1
                if Nb_slash == 3:
                    break
                if Nb_point == 2:
                    break
                if cnt > 7:
                    site += char

    if "www." in site:
        cnt = 0
        new_site =''
        for char in site:
            cnt+=1
            if cnt >4:
                new_site += char
    else:
        new_site =''
        for char in site:
            if char == '.':
                break
            new_site += char

    return new_site

################################################################################

def Find_content_length(line_6):
    cnt = 0
    new_word = ''
    index = 0
    for word in line_6.split():
        index+=1
        if index == 2:
            #print (word)
            for char in word:
                if char == ';':
                    break
                new_word += char


    try:
        content_length = (int(new_word))
    except ValueError:
        content_length = -1
    return (content_length)

################################################################################

def Find_type_of_text(line_5):
    global text_html
    global text_plain
    global text_Not_itdentified
    global text_other
    cnt = 0
    new_word = ''
    index = 0
    for word in line_5.split():
        index+=1
        if index == 2:
            #print (word)
            for char in word:
                if char == ';':
                    break
                new_word += char

    if new_word == '' or new_word == 'Last-modified:':
        new_word = "Not_Identified"
    if new_word == "text/html":
        text_html += 1
        return 1
    if new_word == "text/plain":
        text_plain += 1
        return 2
    if new_word == "Not_Identified":
        text_Not_itdentified += 1
        return 3
    else:
        text_other += 1
        return -1

################################################################################

def Find_Nb_link_pic_table(html_content):

    soup = BeautifulSoup(html_content, 'lxml')
    soup.find_all('a')

    list_link = (soup.find_all('a'))
    list_table = (soup.find_all('table'))
    list_picture = (soup.find_all('img'))

    yield len(list_link)
    yield len(list_table)
    yield len(list_picture)
################################################################################

def check_charset(title):
    cnt = 0
    template = 'a'
    for x in title:
        template = x;
        break
    char = template
    if(ord(char) >= 3584 and ord(char) <= 3711):
        return "Thai"
    if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >=97 and ord(char) <=122) or ord(char)==40 or ord(char) ==10 or ord(char)==32) or (ord(char) >= 45 and ord(char) <= 60):
        return "Eng"
    else:
        return "Other"

################################################################################
def Find_content(html_content):
    content = get_content_total(html_content)
    return content

################################################################################
def get_content_total(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.get_text()
    return text

################################################################################
def Find_line_content(html_content, title):
    content = get_content_total(html_content)
    content = content.strip()
    content= content.split('\n')
    new_content = []
    for line in content:
        if line == '':
            continue
        new_content.append(line)

    if title == 'No_title':
        return len(new_content)
    else:
        return len(new_content) - 1



################################################################################
def Wordcount(content, title, charset):
    global ENG
    global NO_CONTENT
    global OTHER
    global TH

    if (charset == "Thai"):
        #content = Convert_to_Thai(content)
        newtitle = "".join(title.split())
        count_title = Wordcount_Thai(title)
        if title == "No_title":
            count_title =  0
        count_content = Wordcount_Thai(content)
        count_content -= count_title
        TH += 1
        yield count_title
        yield count_content

    elif (charset == "Eng"):
        #content = Convert_to_Eng(content)
        #title = Convert_to_Eng(title)
        count = Wordcount_Eng(content)
        count_title = Wordcount_Eng(title)
        if title == "No_title":
            count_title = 0
        count_content = count - count_title
        #print ("title :", title)

        if count_title == 0 and count_content == 0:
            NO_CONTENT += 1
        else:
            ENG += 1
        yield count_title
        yield count_content

    elif (charset == "Other"):
        OTHER  +=1
        yield -1
        yield -1

################################################################################

def Wordcount_Thai(text):
    global error
    count_word = 0
    stopword =  ["กล่าว","กว่า","กัน","กับ","การ","ก็","ก่อน","ขณะ","ขอ","ของ","ขึ้น","คง","ครั้ง","ความ",
            "คือ","จะ","จัด","จาก","จึง","ช่วง","ซึ่ง","ดัง","ด้วย","ด้าน","ตั้ง","ตั้งแต่","ตาม","ต่อ","ต่าง",
            "ต่างๆ","ต้อง","ถึง","ถูก","ถ้า","ทั้ง","ทั้งนี้","ทาง","ที่","ที่สุด","ทุก","ทํา","ทําให้","นอกจาก","นัก",
            "นั้น","นี้","น่า","นํา","บาง","ผล","ผ่าน","พบ","พร้อม","มา","มาก","มี","ยัง","รวม","ระหว่าง",
            "รับ","ราย","ร่วม","ลง","วัน","ว่า","สุด","ส่ง","ส่วน","สําหรับ","หนึ่ง","หรือ","หลัง","หลังจาก",
            "หลาย","หาก","อยาก","อยู่","อย่าง","ออก","อะไร","อาจ","อีก","เขา","เข้า","เคย","เฉพาะ","เช่น",
            "เดียว","เดียวกัน","เนื่องจาก","เปิด","เปิดเผย","เป็น","เป็นการ","เพราะ","เพื่อ","เมื่อ","เรา","เริ่ม",
            "เลย","เห็น","เอง","แต่","แบบ","แรก","และ","แล้ว","แห่ง","โดย","ใน","ให้","ได้","ไป","ไม่",
			"ไว้","ก","ข","ฃ","ค","ฅ","ฆ","ง","จ","ฉ","ช","ซ","ฌ","ญ","ฎ","ฏ","ฐ","ฑ","ฒ",
			"ณ","ด","ต","ถ","ท","ธ","น","บ","ป","ผ","ฝ","พ","ฟ","ภ","ล","ว","ศ",
            "ษ","ห","ฬ","อ","ฮ", "จาก", "ๆ", "นะ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

    with open('/home/tengmo/crawler_to_server_set_time/crawler/output_thai/git/word-parser-noPartOfSpeech/wordcut2/input.txt' , 'w') as out:
        out.write(text)
    #print(datainput)
    command= os.popen("bash /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/run_java2.bash")
    datainput = command.read()
    #print(datainput)
    with open('/home/tengmo/crawler_to_server_set_time/crawler/output_thai/git/word-parser-noPartOfSpeech/wordcut2/output.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            for row in reader:
                if row['word'] not in stopword:
                    count_word += 1
        except csv.Error:
            error += 1
            return 0
    return count_word

###############################################################################
def Wordcount_Eng(text):
    stopword = ['all', "she'll", 'just', "don't", 'being', 'over', 'through',
    		   'yourselves', 'its', 'before', "he's", "when's", "we've", 'had',
    			'should', "he'd", 'to', 'only', "there's", 'those', 'under',
    			'ours', 'has', "haven't", 'do', 'them', 'his', "they'll", 'get',
    			'very', "who's", "they'd", 'cannot', "you've", 'they', 'not',
    			'during', 'yourself', 'him', 'nor', "we'll", 'like', 'did',
    			"they've", 'this', 'she', 'each', "won't", 'where', "mustn't",
    			"isn't", "i'll", "why's", 'www', 'because', "you'd", 'doing',
    			'some', 'up', 'are', 'further', 'ourselves', 'out', 'what',
    			'for', 'while', "wasn't", 'does', "shouldn't", 'above', 'between',
    			'ever', 'ought', 'be', 'we', 'who', "you're", 'were', 'here',
    			'hers', "aren't", 'by', 'both', 'about', 'would', 'of', 'could',
    			'against', "i'd", "weren't", "i'm", 'com', 'or', "can't", 'own',
    			'into', 'whom', 'down', "hadn't", "couldn't", "wouldn't", 'your',
    			"doesn't", 'from', "how's", 'her', 'their', "it's", 'there',
    			'been', 'why', 'few', 'too', 'themselves', 'was', 'until', 'more',
    			'himself', "where's", "i've", 'with', "didn't", "what's", 'but',
    			'else', 'herself', 'than', "here's", 'he', 'me', "they're",
    			'myself', 'these', "hasn't", 'below', 'r', 'can', 'theirs', 'my',
    			'k', "we'd", 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself',
    	     	'at', 'have', 'in', 'any', 'if', 'again', 'no', 'that', 'when',
    			'same', 'how', 'other', 'which', 'you', "shan't", 'http', 'shall',
    			'our', 'after', "let's", 'most', 'such', 'on', "he'll", 'a', 'off',
    			'i', "she'd", 'yours', "you'll", 'so', "we're", "she's", 'the',
    			"that's", 'having', 'once','.']

    wordcount = {}
    count= 0
    for word in text.split():
        if word.lower() not in stopword:
            count += 1
    return count

################################################################################
def Find_Nb_Word_In_URL(URL):
    cnt =0
    Nb_spacial_char = 0
    for char in URL:
        cnt +=1
        if cnt > 7:
            if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >=97 and ord(char) <=122) or (ord(char) >= 3584 and ord(char) <= 3711) or (ord(char)>= 48 and ord(char) <= 57)):
                Nb_spacial_char +=0
            else:
                if (ord(char) == ord('%')):
                    Nb_spacial_char +=0
                else:
                    Nb_spacial_char +=1
    if (URL[len(URL)-1]) == '/':
        Nb_spacial_char -=1
    return Nb_spacial_char+1

################################################################################


####################################-Rotate-###############################################
cnt_begin = 0
cnt_end = 1
iterator = 0
f = open(file_path, "r")
lineList = f.readlines()
index = -10;
line_1 = ''
line_2 = ''
line_3 = ''
line_4 = ''
line_5 = ''
line_6 = ''
html_content = ''
for line in lineList:
    iterator += 1
    #print line
    index += 1
    if len(line) > 7:
        if str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
            cnt_begin += 1
            index = 1
            No_page +=1
            #print line
    if (cnt_begin - cnt_end == 1) or (iterator == len(lineList)):
        cnt_end +=1

#######################################-Rotate-##############################################
        #Use(line_1, line_2, line_3, line_4, line_5, line_6, html_content)
        title =  Find_title_def(html_content).strip()
        URL, Nb_slash, len_URL = Find_URL_NB_Slash_LenURL(line_1)
        binary_domain = Find_binary_domain(URL)
        site = Find_site(line_1)
        content_length = Find_content_length(line_6)
        text_type = Find_type_of_text(line_5)
        link, table , picture = Find_Nb_link_pic_table(html_content)
        Nb_word_in_URL = Find_Nb_Word_In_URL(URL)
        content = Find_content(html_content)
        count_title, count_content = Wordcount(content, title, check_charset(title))
        line_content = Find_line_content(html_content, title)


        print "URL : ", URL
        print "title : ", title
        print "word_in_title : ", count_title
        print "content_type : ",text_type
        print "content_length: ", content_length
        print "Number_of_word : ", count_content
        print "Number_of_picture : ", picture
        print "Number_of_table : ", table
        print "Number_of_slash_in_URL_path : ", Nb_slash
        print "binary_vector : ", binary_domain
        print "URL_Length : ", len_URL
        print "Number_of_word_in_URL : ", Nb_word_in_URL
        print "Number_of_outgoing : ", link
        print "Numer_of_webpage_in_the_same_site : ", dict_site[site]
        print "Number_of_line_in_content :",line_content
        print "\n"

        json_dict[URL] = {"word_in_title":count_title, "content_type":text_type,"content_length": content_length,
                          "Number_of_word": count_content, "Number_of_picture": picture, "Number_of_table": table,
                          "Number_of_slash_in_URL_path": Nb_slash, "binary_vector":binary_domain,
                           "URL_Length":len_URL,"Number_of_word_in_URL": Nb_word_in_URL ,
                           "Number_of_outgoing": link , "Numer_of_webpage_in_the_same_site":dict_site[site],
                           "Number_of_line_in_content":line_content,
                           "Array_Feature":[count_title,text_type,content_length,count_content,picture,table,
                            Nb_slash,binary_domain,len_URL, Nb_word_in_URL,link,dict_site[site] ]}

############################################################################################
        line_1 = ''
        line_2 = ''
        line_3 = ''
        line_4 = ''
        line_5 = ''
        line_6 = ''
        html_content = ''


    if cnt_begin == cnt_end:
        if index == 1:
            line_1 = line
        if index == 2:
            line_2 = line
        if index == 3:
            line_3 = line
        if index == 4:
            line_4 = line
        if index == 5:
            line_5 = line
        if index == 6:
            line_6 = line
        if index == 7:
            html_content = ''
        if index > 7 :
            html_content += line

############################################################################################



###########################-SUMARY-#########################################################
#print json_dict

with open('/home/tengmo/crawler_to_server_set_time/crawler/result/json/dict2', 'w') as outfile:
     json.dump(json_dict, outfile, sort_keys = True, indent = 4,
               encoding='utf8')

print "#####################################################################################"
print "SUMARY"
print "Total_page :",No_page
print "- HAVE_TITLE : " , HAVE_TITLE
print "- NO_TITLE   : ", NO_TITLE
print "TH : ", TH
print "ENG : ", ENG
print "OTHER LANGUAGE : ", OTHER
print "NO_CONTENT : ", NO_CONTENT
print "\nType_text"
print "text/html : ", text_html
print "text/plain: ", text_plain
print "text/Not_Identified : ", text_Not_itdentified
print "text/other : ", text_other
print "EXECUTE TIME  --- %s seconds ---" % (time.time() - start_time)
print "#####################################################################################"

############################################################################################
