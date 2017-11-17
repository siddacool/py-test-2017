import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title('Sid\'s GUI')

win.resizable(0, 0)


# Button Click()
def clickMe():
    action.configure(text=" Hello - {name}, {number}".format(name=name.get(),
                                                             number=numberChosen.get()))

# Add a Button
action = ttk.Button(win, text="Do Not Press", command=clickMe)
action.grid(column=2, row=1)
# Disable Button
#action.configure(state='disabled')

# Change label
ttk.Label(win, text="Who Are You:").grid(column=0, row=0)

# Combo Box
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 3, 56, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)
# Restrict value typing
numberChosen.configure(state='readonly')

# Adding Textbox
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
# Set Focus
nameEntered.focus()

# Create Checks
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Un Selected', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Selected', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'


# Radio Callback
def radCall():
    radSel=radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)


# Actual radio Buttons
radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W)

# ScrolledText
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)


win.mainloop()
