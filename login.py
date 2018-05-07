from tkinter import *
import tkinter.messagebox as tm
import MySQLdb
import tkinter as tk
import os
#aid = 3
class LoginFrame(Frame):
    #aid = 0
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)
        #self._login_btn_clicked
        self.logbtn = Button(self, text="register", command=self.helloCallBack)
        self.logbtn.grid(columnspan=2)
        #self.aid = 1
        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")

        username = self.entry_username.get()
        password = self.entry_password.get()
        a = 1;
        #data from acc_table
        db = MySQLdb.connect("localhost","karthi","password","Banking" )
        cursor = db.cursor()
        global aid
        sql = "SELECT * FROM acc_table "
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                firstname = row[0]
                lastname = row[1]
                address = row[2]
                acc_type = row[3]
                passw = row[6]
                #aid = row[4]
                #acid = aid
                # print(username, password)
                if username == firstname and password == passw:
                    a=0
                    #return aid
                    break
                    #tm.showinfo("Login info", "Welcome ")
                #else:
                #    tm.showerror("Login error", "Incorrect username")
            if a == 0:
                #tm.showinfo("Login info", "Welcome ")
                #self.aid = row[4]
                aid = row[4]
                root.destroy()
                #print(aid)
                #os.system('python3 welcome.py')
                #return aid
                #main = MainView(root)
                #main.pack()
            else:
                tm.showinfo("Login info", "not a reg user")
        except:
            print ("Error")

    def helloCallBack(self):
        os.system('python3 reg.py')
            #top.destroy()

#if __name__ == '__main__':
root = Tk()
lf = LoginFrame(root)
#command = self._login_btn_clicked
root.wm_geometry("500x500")
    #print (aid)
    #print (aid)
root.mainloop()
#print (aid)
