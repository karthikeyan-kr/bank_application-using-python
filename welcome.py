from tkinter import *
from login import aid
import MySQLdb
#master = Tk()
#aid = 100

import tkinter as tk

db = MySQLdb.connect("localhost","karthi","password","Banking" )
cursor = db.cursor()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    #def show(self):
    #    self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global acc_id
       self.rid = Label(self, text="Reciever ID")
       self.amount = Label(self, text="enter amount")
       #username.pack()
       #password.pack()
       self.entry_rid = Entry(self)
       self.entry_amount = Entry(self)

       self.sendbtn = Button(self, text="Send", command = self._login_btn_clicked)

       self.rid.grid(row=0, sticky=E)
       self.amount.grid(row=1, sticky=E)
       self.entry_rid.grid(row=0, column=1)
       self.entry_amount.grid(row=1, column=1)

       self.sendbtn.grid(row=2, sticky = W, column=1)
       #entry_username.pack()
       #entry_password.pack()
       self.label = tk.Label(text="This is page 1")
       #label.pack(side="top", fill="both", expand=True)
       #label.pack()
       #self.pack()
    def _login_btn_clicked(self):
        # print("Clicked")
        rid = self.entry_rid.get()
        amount = self.entry_amount.get()
        print (rid, amount)
        #add = self.entry_address.get()
        #acc_type = self.entry_acc_type.get()
        #password = self.entry_password.get()
        #bal = 5000
        #print(fname, lname, add, acc_type)
        #data to acc_table
        sql = "select acc_id from acc_table"
        try:
            cursor.execute(sql)
            tm.showinfo("Login info", "Welcome ")
            db.commit()
        except:
            print("error")



class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global aid
       print (aid)
       sql = "SELECT * from acc_table where acc_id = {};".format(aid)
       try:
           cursor.execute(sql)
           results = cursor.fetchall()
          # print(results)
           for row in results:
               firstname = row[0]
               lastname = row[1]
               address = row[2]
               acc_type = row[3]
               aid = row[4]
               balance = row[5]
        #       print(firstname)

       except:
           print ("error")
       label = tk.Label(self, text="Firstname = %s " % firstname)
       label.pack()
       label = tk.Label(self, text="Lastname = %s" % lastname)
       label.pack()
       label = tk.Label(self, text="Address = %s" % address)
       label.pack()
       label = tk.Label(self, text="Account Type = %s" % acc_type)
       #label.pack(side="top", fill="both", expand=True)
       label.pack()
       label = tk.Label(self, text="Balance = %s" % balance)
       label.pack()

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       #label.pack(side="top", fill="both", expand=True)
       label.pack()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="send money", command=p1.lift)
        b2 = tk.Button(buttonframe, text="account details", command=p2.lift)
        b3 = tk.Button(buttonframe, text="statement", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        #p1.show()


if __name__ == "__main__":
    master = Tk()
    #aid = 100
    master.title('Welcome_page')
    #master.geometry('500x500')
    a = Label(master, text='Welcome to the ALK bank')
    a.pack()
    a = Label(master, text=aid)
    a.pack()
    #root = tk.Tk()
    main = MainView(master)
    main.pack(side="top", fill="both", expand=True)
    master.wm_geometry("500x500")
    master.mainloop()
