a = []
for i in range(2):
        t = []
        for j in range(2):
                t.append(input("Enter Element({},{}): ".format(i, j)))
        a.append(t)

for i in range(2):
    for j in range(2):
        print(a[i][j])