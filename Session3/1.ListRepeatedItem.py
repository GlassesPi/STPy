inter_lst = []
union_lst = []

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]

for x in lst1 + lst2:
    if x not in union_lst:
        union_lst.append(x)
for x in union_lst:
    if x in lst1 and x in lst2:
        inter_lst.append(x)

print(inter_lst)
print(union_lst)