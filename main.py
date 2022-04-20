from tkinter import *

root = Tk()
e=Entry(root,width=100,bg="#000",fg="#fff")
e.pack()
e.insert(0,"Enter your name")

def helloWorld():
    val=e.get()
    label1=Label(root,text=val).pack()
lblHello=Label(root,text="Hello world").pack()
btnClick=Button(root,text="Enter your name",padx=50,command=helloWorld,fg="#f2f2f2",bg="#ff0000").pack()


root.mainloop()