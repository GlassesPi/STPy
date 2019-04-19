import time
## With Divide & Conquer

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


n = 30
if n > 0:
    t1 = time.time()
    print(fib(n))
    t2 = time.time()
    print(t2 - t1)
else:
    print('Control')


# With Dynamic Programming

def fib1(n):
    lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i -2])
    return lst[n - 1]

t3 = time.time()
print(fib1(30))
t4 = time.time()
print(t4 - t3)


