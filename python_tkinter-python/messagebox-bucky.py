from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Title', 'Boom Baby')

answer = tkinter.messagebox.askquestion('Tell me', 'Did you take shower today?')

if answer == 'yes':
    print(' :) ')

root.mainloop()