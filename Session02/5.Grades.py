grades = {}
n = int(input("How many subjects do you have? "))

print(" ")

for i in range(n):
    k = input("Name of the subject: ")
    v = float(input("It's grade: "))
    grades[k] = v
    print(" ")

for k, v in grades.items():
    print("{}: {}".format(k, v))

print(" ")

s = 0
for x in grades.values():
    s += x

print("The average is {}".format(s / n))