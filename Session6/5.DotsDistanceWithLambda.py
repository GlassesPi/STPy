from math import sqrt
euclid = lambda a, b: sqrt((sum([pow(a[i] - b[i], 2) for i in range(len(a))])))

def euclid_long(a, b):
    s = 0
    for i in range(len(a)):
        s += pow(a[i] - b[i], 2)
    return sqrt(s)

print(euclid([1, 2], [3, 4]))
print(euclid(10, 20), [3, 4]))

pascal = lambda a: ''.join([x.title() for x in a.split()])
pascal('first name')