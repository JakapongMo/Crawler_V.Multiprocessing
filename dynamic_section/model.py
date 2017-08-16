import sys
import os

arg_1 =  sys.argv[1]
id_date = arg_1
#file_path = '{0}/sub3_{1}.txt'.format(path_dir, arg)
#dict_site = eval(open("{0}/dict_site_{1}.txt".format(path_dir, arg)).read())
path_dir = '/home/tengmo/crawler_to_server_set_time/crawler/result'
cluster =  '{0}/{1}/class/class_{2}'.format(path_dir, id_date, id_date)

#set parameter here#
number_of_round = 1

def read_cluster(id_date):
    ####delete .arc from id_date#####
    id_date = id_date[0:-4]
    path_cluster =  '{0}/{1}/class/class_{2}.json'.format(path_dir, id_date, id_date)
    #print path_cluster
    dict_cluster = eval(open(path_cluster).read())
    #print dict_cluster
    #print len(dict_cluster.keys())
    for k in range(0,len(dict_cluster.keys())):
        #print dict_cluster[str(k)]
        for url_list in dict_cluster[str(k)]:
            print url_list[0]


#########################################################################################
for x in range(0, number_of_round):

    print id_date
    read_cluster(id_date)

    process = os.popen("python find_id.py %s"%id_date)
    id_date = process.read().strip()
    process.close()
    if (id_date == str(0)):
        break
