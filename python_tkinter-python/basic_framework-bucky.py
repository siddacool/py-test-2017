from tkinter import *


def doNothing():
    print('as you wish')

root = Tk()

# Main Menu
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project", command=doNothing)
fileMenu.add_command(label="New", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=doNothing)
editMenu.add_command(label="Copy", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Paste", command=doNothing)


# Toolbar
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Something :(", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Status Bar
status = Label(root, text="wait for it..", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()