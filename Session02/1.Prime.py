import math

n = int(input())

for x in range(2, int(math.sqrt(n))):
    if n % x == 0:
        print("Not Prime")
        break
else:
    print("Prime")






# if not f:
#     print("Prime")
# else:
#     print("Not  Prime")
