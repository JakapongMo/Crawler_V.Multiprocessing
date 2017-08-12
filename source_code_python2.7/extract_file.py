import time
from threading import Thread
import sys
import os

arg = sys.argv[1]
path_dir = "/home/tengmo/crawler_to_server_set_time/crawler/result/%s"%arg
print path_dir

def subMake_Dir():
		command = os.popen("mkdir %s"%path_dir)
		data = command.read()
		command = os.popen("mkdir %s/json"%path_dir)
		data = command.read()
		command = os.popen("mkdir %s/class"%path_dir)
		print("subMake started")

def extract_file():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/ALL_CAL.py")

def subFind_Dict():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/FindDict_arg.py {0}  > {1}/dict_site_{2}.txt".format(arg , path_dir, arg))
		print("subMain1 started")


t = time.time()
t1 = Thread(target=subMake_Dir)
t1.start()
t1.join()


print("done in : ", time.time() -t)
print("Hah... I am done with all work now!")
