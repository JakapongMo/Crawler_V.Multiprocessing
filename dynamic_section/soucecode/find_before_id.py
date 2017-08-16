import sys
import os

store_path = "/home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/store/%s.arc"%sys.argv[1]
name = sys.argv[1]+".arc"

#print name
#print store_path

split_name = name.split("_")
before_id =  int(split_name[0])-1
#print before_id

if (before_id != 0):
    process = os.popen("bash find_before_id.bash {0}".format(before_id))
    before_id = process.read()
    process.close()
print str(before_id).rstrip()
