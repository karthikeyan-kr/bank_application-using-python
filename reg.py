from tkinter import *
import tkinter.messagebox as tm
import MySQLdb
import tkinter as tk

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_fname = Label(self, text="Firstname")
        self.label_lname = Label(self, text="Lastname")
        self.label_address = Label(self, text="Address")
        self.label_acc_type = Label(self, text="Acc_Type")
        self.label_password = Label(self, text="Password")

        self.entry_fname = Entry(self)
        self.entry_lname = Entry(self)
        self.entry_address = Entry(self)
        self.entry_acc_type = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_fname.grid(row=0, sticky=E)
        self.label_lname.grid(row=1, sticky=E)
        self.label_address.grid(row=2, sticky=E)
        self.label_acc_type.grid(row=3, sticky=E)
        self.label_password.grid(row=4, sticky=E)
        self.entry_fname.grid(row=0, column=1)
        self.entry_lname.grid(row=1, column=1)
        self.entry_address.grid(row=2, column=1)
        self.entry_acc_type.grid(row=3, column=1)
        self.entry_password.grid(row=4, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Signup", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)
        #self._login_btn_clicked
        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        fname = self.entry_fname.get()
        lname = self.entry_lname.get()
        add = self.entry_address.get()
        acc_type = self.entry_acc_type.get()
        password = self.entry_password.get()
        bal = 5000
        #print(fname, lname, add, acc_type)
        #data to acc_table
        db = MySQLdb.connect("localhost","karthi","password","Banking" )
        cursor = db.cursor()
        sql = "insert into acc_table (firstname, lastname, address, acc_type, balanc, passw) values ('%s','%s','%s','%s','%d','%s')" % (fname, lname, add, acc_type, bal, password)
        try:
            cursor.execute(sql)
            tm.showinfo("Login info", "Welcome ")
            db.commit()
        except:
            print("error")

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    #def show(self):
    #    self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       #self.lift()
       #label.pack(side="top", fill="both", expand=True)
       label.pack()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1()#self)
        container = tk.Frame()#self)
        container.pack(side="top", fill="both", expand=True)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p1.lift()

root = Tk()
lf = LoginFrame(root)
#command = self._login_btn_clicked
root.wm_geometry("400x400")
root.mainloop()
