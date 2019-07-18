import mysql.connector
from tkinter import *

def saveDB(name,email,age):
    sql = "insert into Student values(null,'{}','{}','{}')".format(name,email,age)
    con = mysql.connector.connect(user='root',password='monu9226',database='pythondb')
    cursor=con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Data Shaved !")

#saveDB('Deepak','deepak123@abc.com',25)


def onClick():  #It shoud be define befor UI Declaration(root = Tk()), After UI Declaration iwil give an error
    name = entryName.get()
    email = entryEmail.get()
    age = entryAge.get()

    saveDB(name,email,age)

    print("Click on Submit Button !")

def show():
    print("This is Awesome")

root = Tk()


menu = Menu(root)
root.config(menu=menu)

fMenu = Menu(menu)
menu.add_cascade(label="File",menu=fMenu)

fMenu.add_command(label="New", command=show)
fMenu.add_command(label="Open")
fMenu.add_command(label="Save")


fEdit = Menu(menu)
menu.add_cascade(label="Edit",menu=fEdit)

fEdit.add_command(label="Cut")
fEdit.add_command(label="Copy")
fEdit.add_command(label="Paste")


fHelp = Menu(menu)
menu.add_cascade(label="Help",menu=fHelp)

lbl = Label(root, text='Welcome to __________________')
lbl.pack()

namelbi = Label(root, text='Enter Your Name....')
namelbi.pack()
entryName = Entry(root)
entryName.pack()

emaillbl = Label(root, text='Enter Your Emali....')
emaillbl.pack()
entryEmail = Entry(root)
entryEmail.pack()

agelbl = Label(root, text='Enter Your Age....')
agelbl.pack()
entryAge = Entry(root)
entryAge.pack()

#btnsubmit = Button(root, text='Submit', command=onClick())  #run onClick Function before clicking on Submit buttom
btnsubmit = Button(root, text='Submit', command=onClick)      #run onClick  Function After clicking on Submit buttom
btnsubmit.pack()

root.mainloop()
