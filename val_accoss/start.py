from tkinter import *

def button():
    global C
    mylabel = Label(myGui, text = "hi").grid(row = 0, column = 0)
    A = B.get()
    C = A


myGui = Tk()
B = StringVar()
C = ""
myentry = Entry(myGui, textvariable = B).grid(row = 1, column = 0)
Submit = Button(myGui, text = "Submit", command = button).grid(row = 1, column = 1)
# and then A is not empty
B = A
mainloop()
