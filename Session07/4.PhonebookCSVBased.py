from tkinter import Label, Entry, Button, Tk
from tkinter.ttk import Treeview
import csv

def show():
    for i in tv.get_children():
        tv.delete(i)

    with open('file.csv', 'r') as csvfile:
        f1 = csv.reader(csvfile, delimiter=',')
        for row in f1:
            tv.insert( "", "end", values=row)

def save():
    with open('file.csv', 'a', newline='') as csvfile:
        f1 = csv.writer(csvfile, delimiter=',')
        f1.writerow([name_entry.get(), phone_entry.get()])
    show()

root = Tk()
Label(root, text="PhoneBook", font=('', 18)).grid(row=0, column=0)

cols = ['Name', 'Phone']
tv = Treeview(root, columns=cols, show='headings')
for col in cols:
    tv.heading(col, text=col)

tv.grid(row=1, column=0, columnspan=2)

Label(root, text ="Name: ").grid(row=3, column=0)

name_entry = Entry(root)
name_entry.grid(row=3, column=1)

Label(root, text="Phone: ").grid(row=4, column=0)

phone_entry = Entry(root)
phone_entry.grid(row=4, column=1)

Button(root, text="Save", command=save).grid(row=5, column=1)
show()
root.mainloop()
