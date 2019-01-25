def factorial(x):
    s = 1
    for i in range(2, x+1):
        s *= i
    return s


n = int(input())
print(factorial(n))
