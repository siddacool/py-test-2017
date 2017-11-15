from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Press This Shit", fg="red")
button2 = Button(topFrame, text="Press This Shit", fg="blue")
button3 = Button(topFrame, text="Press This Shit", fg="green")
button4 = Button(bottomFrame, text="Press This Shit", fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()