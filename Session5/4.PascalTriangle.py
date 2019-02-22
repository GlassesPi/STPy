def fact(x):
    t = 1
    for i in range(2, x + 1):
        t *= i
    return t

def comb(a, b):
    return fact(a) // (fact(b) * fact(a - b))

n = int(input())
for i in range(n):
    for j in range(n - i):
        print(' ', end ='')
    for j in range(i + 1):
        print('{} '.format(comb(i, j)),end='')
    print()