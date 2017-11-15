from tkinter import *

root = Tk()


def printName(event):
    print('Sid')

button_1 = Button(root, text="Say My Name")
button_1.bind('<Button-1>', printName)
button_1.grid(row=0)

root.mainloop()