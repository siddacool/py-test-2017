from tkinter import *


class ButtonsOMine:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Bla", command=self.printMsg)
        self.printButton.pack(side=LEFT)

        self.quiteButton = Button(frame, text="Bye", command=frame.quit)
        self.quiteButton.pack(side=LEFT)

    def printMsg(self):
        print('Bla Bla Bla')


root = Tk()
b = ButtonsOMine(root)
root.mainloop()