import sys
import os

store_path = "/home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/store/%s.arc"%sys.argv[1]
name = sys.argv[1]+".arc"

#print name
#print store_path

split_name = name.split("_")
next_id =  int(split_name[0])+1
#print before_id

process = os.popen("bash find_next_id.bash {0}".format(next_id))
next_id = process.read()
process.close()
print str(next_id).rstrip()
