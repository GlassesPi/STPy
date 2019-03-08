# import sqlite3
# conn = sqlite3.connect('my_db.db')
# c = conn.cursor()
# c.execute("CREATE TABLE phone (name text, phone text)")
# c.execute("INSERT INTO phone VALUES ('John', '123456')")
# conn.commit()
# conn.close()



import sqlite3
conn = sqlite3.connect('my_db.db')
c = conn.cursor()
c.execute('SELECT name, phone FROM phone')
print(c.fetchall())
conn.close()




from tkinter import Label, Entry, Button, Tk
from tkinter.ttk import Treeview
import csv



def show():
    for i in tv.get_children():
        tv.delete(i)

    conn = sqlite3.connect('my_db.db')
    c = conn.cursor()
    c.execute('SELECT * FROM phone')

    for row in c.fetchall():
        tv.insert("", "end", values=row)
    conn.close()


def save():
    conn = sqlite3.connect('my_db.db')
    c = conn.cursor()
    c.execute("INSERT INTO phone VALUES ('{}', '{}')".format(name_entry.get(), phone_entry.get()))
    conn.commit()
    conn.close()
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
