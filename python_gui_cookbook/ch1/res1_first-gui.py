import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Sid\'s GUI')

#win.resizable(0, 0)

# Label
aLabel = ttk.Label(win, text="Just Something")
aLabel.grid(column=0, row=0)

# Button Click()
def clickMe():
    action.configure(text=" You Clicked! ")
    aLabel.configure(text="Dude", foreground='red')

# Add a Button
action = ttk.Button(win, text="Do Not Press", command=clickMe)
action.grid(column=1, row=0)

win.mainloop()