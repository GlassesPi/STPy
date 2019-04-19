# from threading import Thread
from multiprocessing import Process
import os

def do_sth():
    print(os.getpid())


# for i in range(2):
#     t = Thread(target=do_sth)
#     t.start()


for i in range(2):
    t = Process(target=do_sth)
    t.start()