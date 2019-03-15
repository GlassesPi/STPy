from random import random
from math import sqrt
n = 10 ** 10
c = 0
for i in range(n):
    x = random()
    y = random()
    if sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2) <= 0.5:
        c += 1
    
print(c / (n * 0.25))