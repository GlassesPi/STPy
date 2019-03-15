from functools import reduce
lst = list(map(int, input().split()))
print(reduce(lambda x, y: x * y, lst))