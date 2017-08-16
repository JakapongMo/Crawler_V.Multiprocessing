import time
from threading import Thread
import sys
import os

arg = sys.argv[1]
path_dir = "/home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/result/%s"%arg
print path_dir

def subMake_Dir():
		command = os.popen("mkdir %s"%path_dir)
		data = command.read()
		command = os.popen("mkdir %s/json"%path_dir)
		data = command.read()
		command = os.popen("mkdir %s/class"%path_dir)
		print("subMake started")

def subFind_Dict():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/soucecode/FindDict_arg.py {0}  > {1}/dict_site_{2}.txt".format(arg , path_dir, arg))
		print("subMain1 started")

def subLoop_Make_Sub():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/soucecode/loop_arg.py {0} {1}".format(arg, path_dir))
		print("subMain2 started")
def subFind_json():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/soucecode/time_write_json_arg.py {0} {1}".format(arg, path_dir))
		print("subMain3 started")
def subFind_Cluster():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/soucecode/cluster/ALL_Cluster.py {0} {1}".format(arg, path_dir))
		print("subMain4 started")

def subFind_URL_Vector():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/dynamic_section/soucecode/input_cluter_with_name_arg.py {0} {1}".format(arg, path_dir))
		print("subMain4 started")

t = time.time()
t1 = Thread(target=subMake_Dir)
t2 = Thread(target=subFind_Dict)
t3 = Thread(target=subLoop_Make_Sub)
t4 = Thread(target=subFind_json)
t5 = Thread(target=subFind_URL_Vector)
t1.start()
t1.join()

t2.start()
t2.join()

t3.start()
t3.join()

t4.start()
t4.join()

t5.start()
t5.join()


print("done in : ", time.time() -t)
print("Hah... I am done with all work now!")
