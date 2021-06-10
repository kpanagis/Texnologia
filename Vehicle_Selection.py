Class Vehicle_Selection()
menu = {}
menu['1']="Add Vehicle." 
menu['2']="Delete Vehicle."
menu['3']="Select Vehicle"
menu['4']="Exit"
while True: 
  options=menu.keys()
  options.sort()
    for entry in options: 
      print entry, menu[entry]

    selection=raw_input("Select:") 
    if selection =='1': 
      print "add" 
    elif selection == '2': 
      print "delete"
    elif selection == '3':
      print "select" 
    elif selection == '4': 
      break
    else: 
      print "Unknown Option Selected!"

def Add_Vehicle():
   import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="Users_Vehicles"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Users_Vehicles (Vehicle, plates) VALUES (%s, %s)"
val = ("minicooper", "AAA 1234")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

def Remove_Vehicle():
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="Users_Vehicles"
)

mycursor = mydb.cursor()

sql = "DELETE FROM Users_Vehicles WHERE address = 'monopanagis'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


def Select_Vehicle()
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="Users_Vehicles"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Users_Vehicles")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
