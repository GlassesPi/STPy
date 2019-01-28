lst = []
i = 0
s = 0
e = 0
n = int(input('How many numbers you want to add? '))

while i < n:
    lst.append(int(input("Please enter {}'th number: ".format(i+1))))
    i += 1

i = 0

#Sum
while i < len(lst):
    s += lst[i]
    i += 1

#Avg
avg = s / n

i = 0
s = 0

#Zigma
while i < n:
    e += ((lst[i] - avg)**2)
    i += 1
e = e / n

print('The Sum is -> {} and the Avg is -> {} and the Zigma is -> {} '.format(s, avg, e))
