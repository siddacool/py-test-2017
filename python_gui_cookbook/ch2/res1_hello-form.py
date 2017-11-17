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
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

# ScrolledText
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3,  sticky='WE')

# Label Container
labelsFrame = ttk.LabelFrame(win, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=20, pady=40)

# Add labels to container
ttk.Label(labelsFrame, text='Label 1').grid(column=0, row=0)
ttk.Label(labelsFrame, text='Label 2').grid(column=0, row=1)
ttk.Label(labelsFrame, text='Label 3').grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)



win.mainloop()
