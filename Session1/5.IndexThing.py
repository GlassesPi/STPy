# n = int(input('How many numbers you want to add? '))
# z = list(range(n))
# # while i < n:
# #     lst.append(int(input("Please enter {}'th number: ".format(i+1))))
# #     i += 1

# s = int(input('Which number?')

# for i in z:
#     if z[i] == s:
#         print("The index is {} ".format(i))
#         break

lst = [1,2,3,4]
x = 3
for i in range(len(lst)):
    if x == lst[i]:
        print("{} is in {}th index".format(x, i))