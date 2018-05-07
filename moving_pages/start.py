import sys
import os
import tkinter
top = tkinter.Tk()

def helloCallBack():
    os.system('python3 end.py')
    top.destroy()


#root = tkinter.Tk()
#frame = tkinter.Frame(root)
#frame.pack()

#button = tkinter.Button(frame)
#button['text'] ="Good-bye."
#button['command'] = helloCallBack
#button.pack()
B = tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()
