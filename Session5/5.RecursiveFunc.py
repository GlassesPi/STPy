def power(a,b):
    if b == 1:
        return a
    else:
        return power(a, b-1) * a


print(power(2,3))