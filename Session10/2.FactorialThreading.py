from threading import Thread
# from multiprocessing import Process
import os

def do_sth():
    print(os.getpid())

def fact(x):
    s = 1
    for j in range(2, x+1):
        s *= j
    print('{} factorial is {}'.format(x, s))



for i in range(4):
    n = int(input())
    fact(n)
    t = Thread(target=fact, args=[n])
    t.start()


# for i in range(2):
#     t = Process(target=do_sth)
#     t.start()