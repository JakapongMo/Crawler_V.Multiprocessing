import time
from threading import Thread
import sys
import os

arg = sys.argv[1]
path_dir = sys.argv[2]


def subMain1():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/cluster/input_cluter_arg.py {0} {1} > {2}/input_vector_{3}.txt".format(arg, path_dir ,path_dir, arg))
		print("subMain1 started")

def subMain2():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/cluster/input_cluter_with_name_arg.py  {0} {1} > {2}/input_vector_with_name_{3}.txt".format(arg, path_dir ,path_dir, arg))
		print("subMain2 started")

def subMain3():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/cluster/xmeans_examples_arg.py {0} {1} > {2}/center_{3}.txt".format(arg, path_dir, path_dir, arg))
		print("subMain3 started")

def subMain4():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/cluster/cal_cluster_arg.py {0} {1} ".format(arg, path_dir))
		print("subMain4 started")

t = time.time()
#calc_square(arr)
#calc_cube(arr)
t1 = Thread(target=subMain1)
t2 = Thread(target=subMain2)
t3 = Thread(target=subMain3)
t4 = Thread(target=subMain4)
t1.start()
t1.join()

t2.start()
#t3.start()
#t4.start()

t2.join()
t3.start()
t3.join()
t4.start()
t4.join()
