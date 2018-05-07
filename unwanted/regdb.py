import MySQLdb
db = MySQLdb.connect("localhost","karthi","password","Banking" )
fname = "karthi"
lname = "kr"
add = "chennai"
acc_type = "saving"
password = 2345
bal = 5000
cursor = db.cursor()
sql = "insert into name values ('%s')" % (fname)
try:
    cursor.execute(sql)
     #cursor.execute("INSERT INTO name VALUES (%s)", (fname))
    db.commit()
    #tm.showinfo("Login info", "Welcome ")
except:
    print("error")
