import MySQLdb
from tkinter import *
#colours = ['red','green','orange','white','yellow','blue']

#r = 0
#for c in colours:
#    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
#    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
#    r = r + 1

#mainloop()
#def close_window():
#    window.destroy()
#mg.geometry('450*450')
db = MySQLdb.connect("localhost","karthi","password","Banking" )
cursor = db.cursor()
sql = "SELECT * FROM acc_table"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        firstname = row[0]
        lastname = row[1]
        address = row[2]
        acc_type = row[3]
        print ("fname = %s, lname = %s, address = %s, " %(firstname, lastname, address))
#cursor.execute("SELECT VERSION ()")
except:
    print ("Error")
#data = cursor.fetchone()
#print ("Database version : %s " % data)
db.close()
