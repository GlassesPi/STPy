d = {5:20, 'a':11, 3:'bc', 6:[1,2,3]}

print(d.keys())
print(d.values())
print(d.items())

for k,v in d.items():
    print(str(k) + " => " + str(v))

# i = 0
# for v in d.items():
#     print(v[i])
#     if i < len(d.keys()):
#         i += 1