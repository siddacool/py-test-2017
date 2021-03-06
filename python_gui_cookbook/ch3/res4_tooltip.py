import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def createToolTip( widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


win = tk.Tk()
win.title('Sid\'s GUI')

# Icon
win.iconbitmap(r'py.ico')

win.resizable(0, 0)

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill='both')

# Monty Sub
monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)

# Monty2 Sub
monty2 = ttk.LabelFrame(tab2, text=' Holy Balls ')
monty2.grid(column=0, row=0, padx=8, pady=4)

# Who Are You
ttk.Label(monty, text="Who Are You:").grid(column=0, row=0)
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()

# Choose a number
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 3, 56, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)
numberChosen.configure(state='readonly')


# Do Not Press
def clickMe():
    action.configure(text=" Hello - {name}, {number}".format(name=name.get(),
                                                             number=numberChosen.get()))

action = ttk.Button(monty, text="Do Not Press", command=clickMe)
action.grid(column=2, row=1)


# Create Checks
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty2, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty2, text='Un Selected', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty2, text='Selected', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Create Checks Radiobuttons
colors = ['Blue', 'Gold', 'Red']


def radCall():
    radSel=radVar.get()
    if radSel == 0:
        monty2.configure(text=colors[0])
    elif radSel == 1:
        monty2.configure(text=colors[1])
    elif radSel == 2:
        monty2.configure(text=colors[2])


radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

# Spinbox Widget
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin = Spinbox(monty, from_=0, to=10, width=5, bd=8, command=_spin)
spin.grid(column=0, row=2)
createToolTip(spin, 'This is a Spin control.')

# ScrolledText
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Labels
labelsFrame = ttk.LabelFrame(monty2, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7)

ttk.Label(labelsFrame, text='Label 1').grid(column=0, row=0)
ttk.Label(labelsFrame, text='Label 2').grid(column=0, row=1)
ttk.Label(labelsFrame, text='Label 3').grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# Left align children
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