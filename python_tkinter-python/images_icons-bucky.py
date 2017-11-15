from tkinter import *

root = Tk()

photo = PhotoImage(file="capture.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()