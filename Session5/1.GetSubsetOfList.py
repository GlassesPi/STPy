lst = ['a', 'b', 'c']
bins = []
for i in range(pow(2,len(lst))):
    x = bin(i).replace('0b', '')
    while len(x) < len(lst):
        x = '0' + x
    bins.append(x)

for x in bins:
    t = []
    for i in range(len(lst)):
        if x[i] == '1':
            t.append(lst[i])
    print(t)