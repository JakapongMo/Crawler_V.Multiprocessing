import time
from threading import Thread
import sys
import os

arg = sys.argv[1]
path_dir = sys.argv[2]

def subMain1():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/write_json_arg.py {0} {1}".format(arg, path_dir))
		print("subMain1 started")

def subMain2():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/write_json_arg2.py {0} {1}".format(arg, path_dir))
		print("subMain2 started")
def subMain3():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/write_json_arg3.py {0} {1}".format(arg, path_dir))
		print("subMain3 started")
def subMain4():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/write_json_arg4.py {0} {1}".format(arg, path_dir))
		print("subMain4 started")
t = time.time()
#calc_square(arr)
#calc_cube(arr)
z1 = Thread(target=subMain1)
z2 = Thread(target=subMain2)
z3 = Thread(target=subMain3)
z4 = Thread(target=subMain4)
z1.start()
z2.start()
z3.start()
z4.start()

z1.join()
z2.join()
z3.join()
z4.join()
print("done in : ", time.time() -t)
print("Hah... I am done with all work now!")
