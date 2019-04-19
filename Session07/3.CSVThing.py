import csv
with open('file.csv') as csvfile:
    f1 = csv.reader(csvfile, delimiter=',')
    for row in f1:
        print(row)


with open('file.csv', 'a', newline='') as csvfile:
    f1 = csv.writer(csvfile, delimiter=',')
    f1.writerow(['ghir', 789])
