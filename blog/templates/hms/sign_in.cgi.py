import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="myne"
    )
print(mydb)
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE python(name varchar(20),email varchar(30))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
sql="INSERT INTO python(name,email) VALUES(%s,%s)"
val=("john","Phagwara 144401")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
mycursor.execute("SELECT* from python")
myresult=mycursor.fetchall()
for  x in myresult:
    print(x)
create="CREATE TABLE "
#mycursor.execute(create+"new(id INT AUTO_INCREMENT PRIMARY KEY,name varchar(200),school varchar(200),mob varchar(20))")

#mycursor.execute("ALTER TABLE new ADD COLUMN email v")
val2=(
    ("juta","ck810295"),
    ("pranav","paranav8192.com"),
    ("amit","atkr70@gmail.com")
    )
mycursor.executemany("INSERT INTO new (name,school) VALUES(%s,%s)",val2)
mydb.commit()
print("record inserted succesfully with last id:",mycursor.lastrowid, mycursor.rowcount)
