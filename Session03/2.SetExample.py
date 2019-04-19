s = set()
s.add(1)
s.add(1)
s.add(2)

print(s)

####################

lst = [1,2,3,4,5,5,6,6,1]
print(set(lst))

####################

a = set("abcd")
b = set("de")
a.difference(b)
a.union(b)
a.intersection(b)
a.issubset(b)
a.issuperset(b)
a.remove(val)       #if val not in: error
a.discard(val)      #no error
a.isdisjoint(b)
###################

a = {1, 2}
b = {3, 4}
a.remove(1)
print(a)
