from tkinter import *

root = Tk()

one = Label(root, text="One", bg="green", fg="white")
one.pack()
two = Label(root, text="Two", bg="red", fg="black")
two.pack(fill=X)
three = Label(root, text="three", bg="blue", fg="black")
three.pack(side=LEFT, fill=Y)

root.mainloop()