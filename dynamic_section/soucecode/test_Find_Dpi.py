########calculate the vector that you input and vectore id before your input
########How to use it : python model.py 1_01_01_2017.arc   -> output will be create vector_interval id 1 and id 0
import sys
import os

arg_1 =  sys.argv[1]
id_date = arg_1
#file_path = '{0}/sub3_{1}.txt'.format(path_dir, arg)
#dict_site = eval(open("{0}/dict_site_{1}.txt".format(path_dir, arg)).read())
path_dir = '/home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/result'
cluster =  '{0}/{1}/class/class_{2}'.format(path_dir, id_date, id_date)

#set parameter here#
number_of_round = 1

def read_static(id_date):
    ####delete .arc from id_date#####
    id_date = id_date[0:-4]
    path_static =  '{0}/{1}/class/id_vector_with_URL_{2}.txt'.format(path_dir, id_date, id_date)
    #print path_cluster
    dict_static = eval(open(path_static).read())
    for key, value in dict_static.iteritems():
        print value

def Find_Dpi(dict_static, dict_static_next ,interval_vector_before, k, a, b):

    same = 0
    list_index = [12,3,4,5,10]
    for x in list_index:
        if (dict_static_next[k][x] == dict_static[k][x]):
            same = same + 1
    if (interval_vector_before[k][17] == (float(b)/(a+b))):
        same = same + 1
    #return (float(1) - ((2*same)/12))
    return (float(1) - (float(2*same)/12))
def cal_two_id_date(id_date, next_id_date):
    id_date = id_date[0:-4]
    next_id_date = next_id_date[0:-4]
    split_id_1 = id_date.split("_")
    split_id_2 = next_id_date.split("_")
    path_static_next =  '{0}/{1}/class/id_vector_with_URL_{2}.txt'.format(path_dir, next_id_date, next_id_date)
    dict_static_next = eval(open(path_static_next).read())
    if (split_id_1[0] != 0):
        path_static =  '{0}/{1}/class/id_vector_with_URL_{2}.txt'.format(path_dir, id_date, id_date)
        dict_static = eval(open(path_static).read())

    #for key, value in dict_static_next.iteritems():
    #    print value
    print split_id_1[0]

    if (split_id_1 != 0):
        pathe_interval_vector_before = "{0}/vector_interval/id_vector_with_URL_{1}_{2}.txt".format(path_dir, int(split_id_1[0])-1, int(split_id_2[0])-1)
        interval_vector_before = eval(open(pathe_interval_vector_before).read())
    #with open("{0}/vector_interval/id_vector_with_URL_{1}_{2}.txt".format(path_dir, split_id_1[0], split_id_2[0]) , 'w') as out:
    #    out.write("{")
        for k,v in dict_static_next.items():
    #        out.write("\"")
    #        out.write(str(k))
    #        out.write("\"")
    #        out.write(":")
            #a = [int(dict_static_next[k][12]) - int(dict_static[k][12])]

            #### if id befor == id 0
            if (int(split_id_1[0]) == 0):
                a = 0
                b = 1
                Dpi = 1

            #### id id before != 0
            if (int(split_id_1[0]) != 0):
                a = interval_vector_before[k][19]
                b = interval_vector_before[k][20]
                Dpi = Find_Dpi(dict_static, dict_static_next ,interval_vector_before, k, a, b)
                if (v == dict_static[k]):
                    a = a+1
                else:
                    b = b+1


            print Dpi
            '''
            ####if id ==1 (id before == 0)
            if (int(split_id_2[0]) == 1):
                list_a = [dict_static_next[k][0],dict_static_next[k][1],dict_static_next[k][2],dict_static_next[k][3],dict_static_next[k][4],dict_static_next[k][5],dict_static_next[k][6],dict_static_next[k][7],dict_static_next[k][8],dict_static_next[k][9],dict_static_next[k][10],dict_static_next[k][11],dict_static_next[k][12],dict_static_next[k][12],dict_static_next[k][3] ,dict_static_next[k][4],dict_static_next[k][5] ,int(b)/(int(a)+int(b)), dict_static_next[k][10], a, b]
            else:
                list_a = [dict_static_next[k][0],dict_static_next[k][1],dict_static_next[k][2],dict_static_next[k][3],dict_static_next[k][4],dict_static_next[k][5],dict_static_next[k][6],dict_static_next[k][7],dict_static_next[k][8],dict_static_next[k][9],dict_static_next[k][10],dict_static_next[k][11],dict_static_next[k][12],int(dict_static_next[k][12]) - int(dict_static[k][12]),int(dict_static_next[k][3]) - int(dict_static[k][3]),int(dict_static_next[k][4]) - int(dict_static[k][4]),int(dict_static_next[k][5]) - int(dict_static[k][5]), int(b)/(int(a)+int(b)) ,int(dict_static_next[k][10]) - int(dict_static[k][10]), a, b ]
            out.write(str(list_a))
            out.write(",")
            out.write('\n')
        out.write("}")
            '''


######################################################################################### MAIN ###############################################################
for x in range(0, number_of_round):

    #read_static(id_date)

    process = os.popen("python find_next_id.py %s"%id_date)
    before_id_date = id_date
    id_date = process.read().strip()
    process.close()

    print before_id_date
    print id_date
    cal_two_id_date(before_id_date, id_date)

    if (id_date == str(0)):
        break



#find source of url in cluster####
'''
def read_cluster(id_date):
    ####delete .arc from id_date#####
    id_date = id_date[0:-4]
    path_cluster =  '{0}/{1}/class/id_vector_with_URL_{2}.txt'.format(path_dir, id_date, id_date)
    #print path_cluster
    dict_cluster = eval(open(path_cluster).read())
    #print dict_cluster
    #print len(dict_cluster.keys())
    for k in range(0,len(dict_cluster.keys())):
        #print dict_cluster[str(k)]
        for url_list in dict_cluster[str(k)]:
            print url_list[0]
'''
