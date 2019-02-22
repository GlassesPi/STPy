def power(a,b):
    if b == 1:
        return a
    else:
        return power(a, b-1) * a


def power1(a,b):
    if b == 1:
        return a
    else:
        if b % 2 == 0:
            x = power1(a, b //2)
            return x * x
        else:
            return power1(a, b // 2) * power1(a, b // 2 + 1)

def power2(a,b):
    if b == 1:
        return a
    else:
        return power2(a, b // 2) * power2(a, b - b // 2)

print(power(2,3))
print(power1(2,3))
print(power2(2,3))