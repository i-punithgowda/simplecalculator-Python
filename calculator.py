from tkinter import *

root=Tk()
root.title("Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,columnspan=3)


def  btnClick(n):
    old=e.get()
    e.delete(0,END)
    e.insert(0,str(old)+str(n))
def btnClear():
    e.delete(0,END)

def btnEqual():
    l=[]
    for i in e.get():
       l.append(int(i))
    e.delete(0,END)
    e.insert(0,sum(l))

button1=Button(text="1",padx=40,pady=20,command=lambda: btnClick(1))
button2=Button(text="2",padx=40,pady=20,command=lambda: btnClick(2))
button3=Button(text="3",padx=40,pady=20,command=lambda: btnClick(3))
button4=Button(text="4",padx=40,pady=20,command=lambda: btnClick(4))
button5=Button(text="5",padx=40,pady=20,command=lambda: btnClick(5))
button6=Button(text="6",padx=40,pady=20,command=lambda: btnClick(6))
button7=Button(text="7",padx=40,pady=20,command=lambda: btnClick(7))
button8=Button(text="8",padx=40,pady=20,command=lambda: btnClick(8))
button9=Button(text="9",padx=40,pady=20,command=lambda: btnClick(9))
button0=Button(text="0",padx=40,pady=20,command=lambda: btnClick(0))
buttonEqual=Button(text="=",padx=140,pady=20,command=btnEqual)
buttonClear=Button(text="C",padx=85,pady=20,command=btnClear)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonClear.grid(row=4,column=1,columnspan=2)
buttonEqual.grid(row=5,column=0,columnspan=3)
root.mainloop()