import time
from threading import Thread
import sys
import os


def subMain1():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/write_json.py > json1.txt")
		print("subMain1 started")

def subMain2():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/write_json2.py > json2.txt")
		print("subMain2 started")
def subMain3():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/write_json3.py > json3.txt")
		print("subMain3 started")
def subMain4():
		command = os.popen("python /home/tengmo/crawler_to_server_set_time/crawler/source_code_python2.7/write_json4.py > json4.txt")
		print("subMain4 started")
t = time.time()
#calc_square(arr)
#calc_cube(arr)
t1 = Thread(target=subMain1)
t2 = Thread(target=subMain2)
t3 = Thread(target=subMain3)
t4 = Thread(target=subMain4)
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
print("done in : ", time.time() -t)
print("Hah... I am done with all work now!")
