from multiprocessing import Process
import time


def do_sum(q, b, e):
    s = b
    for i in range(b + 1, e + 1):
        s += i
    q.put(s)
    # print(s)


n = int(input())
t1 = time.time()
s = 0
for i in range(1, n + 1):
    s += i
t2 = time.time()
print('Linear: ', t2 - t1)
print('Linear: ', s)
q = Queue()
t1 = time.time()
p1 = Process(target=do_sum, args=[q, 1, n // 2])
p2 = Process(target=do_sum, args=[q, n // 2 + 1, n])
p1.start()
p2.start()
p1.join()
p2.join()
s = 0
for _ in range(q.qsize()):
    s += q.get()
t2 = time.time()
print('Parallel: ', t2-t1)
print('Parallel: ', s)