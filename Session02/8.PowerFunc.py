def Power(a, b):
    s = 1
    for _ in range(b):
        s *= a
    return s


x = int(input())
s = int(input())
print(Power(x,s))
