import sys
reload(sys)
import os
sys.setdefaultencoding('utf8')
file_path = '/home/tengmo/crawler_to_server_set_time/crawler/store/%s.arc'%sys.argv[1]
#output_path = '/home/tengmo/crawler_to_server_set_time/crawler/result/dict_site_%s.txt'%sys.argv[1]



############################################################################################
def Use(line_1, line_2, line_3, line_4, line_5, line_6, html_content):
    print line_1
    #print line_2
    print line_3
    #print line_4
    #print line_5
    #print line_6
    print html_contents

############################################################################################

def Find_site(line_1):
    URL = ''
    Nb_point =0
    Nb_slash =0

    cnt = 0
    for char in line_1:
        cnt +=1
        if char == ' ':
            break
        if char == '.':
            Nb_point +=1
        if char == '/':
            Nb_slash +=1
        if Nb_slash == 3:
            break
        if Nb_point == 2:
            break
        if cnt > 7:
            URL += char
    if "www." in URL:
        cnt = 0
        new_URL =''
        for char in URL:
            cnt+=1
            if cnt >4:
                new_URL += char
    else:
        new_URL =''
        for char in URL:
            if char == '.':
                break
            new_URL += char
    return new_URL

############################################################################################

######################################-MAIN-VARIABLE-##################################
my_dict = {}

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
            #print line
    if (cnt_begin - cnt_end == 1) or (iterator == len(lineList)):
        cnt_end +=1

###############################-MAIN-RotateFuntion-######################################
        site = Find_site(line_1)
        if site in my_dict:
            my_dict[site] += 1
        else:
            my_dict[site] = 1

#########################################################################################

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

print (str(my_dict))
with open(output_path , 'w') as out:
    out.write("{")
    for k,v in my_dict.items():
        out.write("\"")
        out.write(str(k))
        out.write("\"")
        out.write(":")
        out.write(str(v))
        out.write(",")
        out.write('\n')
    out.write("}")
