import mysql.connector
class Student:
    def __init__(self,roll,name,email,age):
        self.roll = roll
        self.name = name
        self.email = email
        self.age = age

    def showStudent(self):
        data = "Roll no. is  {},  Name is  {} ,   Email is {}   and     age is  {}".format(self.roll,self.name,self.email,self.age)
        print(data)

    def getStudentDetails(self):
        data = "Roll no. is  {},  Name is  {} ,   Email is {} and age is  {} /n".format(self.roll,self.name,self.email,self.age)
        return data

s1 = Student(101,"Deepesh","deepesh@abc.com",24)
s1.showStudent()

""""
#Readin and writng data into file

#with open("mySql.txt","a") as file: # For reding file
#file.write(s1.getStudentDetails())
file = open("mySql.txt","r")  #for writing File
dataRead = file.readlines()
print(dataRead)
file.close()
"""

#  Reading And Writing Data in Database
con = mysql.connector.connect(user="root",password="monu9226",host="127.0.0.1",database="pythondb")
#print(con.is_connected())

cursor = con.cursor()
#print(cursor)

#sql = "insert into firstmysql.employee values(null ,{}, {}, {})".format(s1.name,s1.email,s1.age)

#***************Insert Data***********
#sqlinsert = "insert into Student values(null,'Deepesh','deep@abc,com',26)"
#***************Delete Data***********
#sqldel = "delete from Student "
#***************Update Data***********
#sqlupdate = "update Student set name = 'sonu', email='sonu123@abc.com' where id =1"

#***************Retrieve Data***********
sqlretrieve = "select * from Student"
cursor.execute(sqlretrieve)
#con.commit() #for only insert, delete create and Update not for retrieve

#**********to retrive single row********
row= cursor.fetchone()
print(row)

#**********to retrieve all rows*********
#for i in cursor:
  #  print(i)

#print("Data saved !!")