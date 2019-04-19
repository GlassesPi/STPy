from tkinter import Tk, Label, Entry, Button

root = Tk()
root.title("Calculator")

label1 = Label(root, text="First Number: ")
label1.grid(row=0, column=0)

num1 = Entry(root)
num1.grid(row=0, column=1)

label2 = Label(root, text="Second Number: ")
label2.grid(row=1, column=0)

num2 = Entry(root)
num2.grid(row=1, column=1)

def add_func():
    n1 = float(num1.get())
    n2 = float(num2.get())
    answer = n1 + n2
    answer_label.configure(text=answer)

calculate_button = Button(root, text="Sum", command=add_func)
calculate_button.grid(row=2, column=1)

label3 = Label(root, text="Result: ")
label3.grid(row=3, column=0)

answer_label = Label(root, text="---")
answer_label.grid(row=3, column=1)
root.mainloop()

