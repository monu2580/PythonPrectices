from tkinter import *
import googlemaps

def onBtnclick():
    srcLoc=entryPick.get()
    destLoc=entryDrop.get()


    pass

root = Tk()
root.config(background="aqua")

lblTitle = Label(root,text="Ola Vs Uber",font=("Helvetica", 25,"bold","underline"),foreground="red",)
lblTitle.pack()

entryxyz3 = Label(root,background="aqua",height=2,width=2)
entryxyz3.pack()


lblPickLoc = Label(root,text="Enter Source Location :",font=("Helvetica", 16,"bold"),foreground="blue")
lblPickLoc.pack()

entryxyz4 = Label(root,background="aqua",height=1,width=2)
entryxyz4.pack()


entryPick = Entry(root,font=("Helvetica", 16))
entryPick.configure({"background": "black","foreground":"white","width":"40"})
entryPick.pack()

entryxyz2 = Label(root,background="aqua",height=1,width=2)
entryxyz2.pack()


lblDropLoc = Label(root,text="Enter Destinition Location :",font=("Helvetica", 16,"bold"),foreground="blue")
lblDropLoc.pack()

entryxyz6 = Label(root,background="aqua",height=1,width=2)
entryxyz6.pack()


entryDrop = Entry(root,font=("Helvetica", 16))
entryDrop.configure({"background": "black","foreground":"white","width":"40"})
entryDrop.pack()

entryxyz1 = Label(root,background="aqua",height=2,width=2)
entryxyz1.pack()


btnSubmit = Button(root,text="Compare Fares" ,font=("Helvetica", 16,"bold"),foreground="green",background="black")
btnSubmit.pack()

entryxyz = Label(root,background="aqua",height=2,width=2)
entryxyz.pack()

entryOutput = Label(root,height=100,width=200, wraplength=200 ,font=("Helvetica", 10,"bold"),foreground="red",background="aqua")
entryOutput.pack()



root.mainloop()
