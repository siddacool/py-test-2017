import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

win = tk.Tk()
win.title('Sid\'s GUI')

win.resizable(0, 0)

# Sub Container
monty = ttk.LabelFrame(win, text=" Monty Python ")
monty.grid(column=0, row=0)


# Button Click()
def clickMe():
    action.configure(text=" Hello - {name}, {number}".format(name=name.get(),
                                                             number=numberChosen.get()))


# Add a Button
action = ttk.Button(monty, text="Do Not Press", command=clickMe)
action.grid(column=2, row=1)

# Change label
ttk.Label(monty, text="Who Are You:").grid(column=0, row=0)

# Change label
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 3, 56, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)
# Restrict value typing
numberChosen.configure(state='readonly')

# Adding Textbox
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
# Set Focus
nameEntered.focus()

# Create Checks
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text='Un Selected', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text='Selected', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
colors = ['Blue', 'Gold', 'Red']


# Radio Callback
def radCall():
    radSel=radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])


# Actual radio Buttons
radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

# ScrolledText
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Label Container
labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7)

# Add labels to container
ttk.Label(labelsFrame, text='Label 1').grid(column=0, row=0)
ttk.Label(labelsFrame, text='Label 2').grid(column=0, row=1)
ttk.Label(labelsFrame, text='Label 3').grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

for child in monty.winfo_children():
    child.grid_configure(sticky='w')

# Reset SRC position
scr.grid_configure(sticky='WE')


# Menu Bar
def _quit():
    win.quit()
    win.destroy()
    exit()

menuBar = Menu(win)
win.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help")
menuBar.add_cascade(label="Help", menu=helpMenu)


win.mainloop()
