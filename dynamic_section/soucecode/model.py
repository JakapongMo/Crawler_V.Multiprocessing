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

def cal_two_id_date(before_id_date, id_date):
    path_static_before =  '{0}/{1}/class/id_vector_with_URL_{2}.txt'.format(path_dir, before_id_date, before_id_date)
    path_static =  '{0}/{1}/class/id_vector_with_URL_{2}.txt'.format(path_dir, id_date, id_date)
    dict_static_before = eval(open(path_static_before).read())
    dict_static = eval(open(path_static).read())
    for key, value in dict_static.iteritems():
        print value

#########################################################################################
for x in range(0, number_of_round):

    #read_static(id_date)

    process = os.popen("python find_next_id.py %s"%id_date)
    next_id_date = id_date
    id_date = process.read().strip()
    process.close()

    print next_id_date
    print id_date

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
