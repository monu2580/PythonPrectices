from tkinter import *
from uber_rides import *


def onSubmit():
    Longi = longiTxt.get()
    Lati = latiTxt.get()
    dispLbl.configure(text="Fair result")
    print("Longitude is ",Longi,'  Latitude is  ',Lati)


root = Tk()
root.title("Fair Comparision between Ola and Uber")
root.maxsize(width=5000,height=3000)

longiLbl = Label(root,text="Enter Longitude")
longiLbl.pack()
longiTxt = Entry(root)
longiTxt.pack()

latiLbl = Label(root,text="Enter Latitude")
latiLbl.pack()
latiTxt = Entry(root)
latiTxt.pack()

#getBtn = Button(root, text="Get Fare", command=onSubmit)
getBtn = Button(root, text="Get Fare", command=onSubmit)
getBtn.pack()

dispLbl = Label(root)
dispLbl.pack()

root.mainloop()