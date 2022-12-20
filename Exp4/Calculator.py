#9
from tkinter import*


def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

def btnAdd():
    global operator
    operator="+"
    text_Input.set(operator)

def btnSub():
    global operator
    operator="-"
    text_Input.set(operator)

def btnMul():
    global operator
    operator="*"
    text_Input.set(operator)

def btnDiv():
    global operator
    operator="/"
    text_Input.set(operator)

def btnPow():
    global operator
    operator="**"
    text_Input.set(operator)

def btnSqrt():
    global operator
    operator="sqrt"
    text_Input.set(operator)

def percent():
    global operator
    operator="%"
    text_Input.set(operator)

def btnPoint():
    global operator
    operator="."
    text_Input.set(operator)

root=Tk()

root.geometry("160x290")
root.title("CALCULATOR")
operator=""
text_Input=StringVar()
metext=Entry(root,font=("Courier New",15,'bold'),width=13,bd=5,bg='white',textvariable=text_Input)
metext.pack(anchor="nw")
but_c=Button(root,bd=4,text="C",font=("Courier New",16,'bold'),bg="dark grey", command=btnClearDisplay)
but_c.place(x=0,y=40)
but_rt=Button(root,bd=4,text="√",font=("Courier New",16,'bold'),bg="dark grey", command=btnSqrt)
but_rt.place(x=40,y=40)
but_sq=Button(root,bd=4,text="x^y",height=2,width=3,bg="dark grey", command=btnPow)
but_sq.place(x=80,y=40)
but_p=Button(root,bd=4,text="%",font=("Courier New",16,'bold'),bg="dark grey", command=percent)
but_p.place(x=120,y=40)
but1=Button(root,bd=4,text="1",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(1))
but1.place(x=0,y=90)
but2=Button(root,bd=4,text="2",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(2))
but2.place(x=40,y=90)
but3=Button(root,bd=4,text="3",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(3))
but3.place(x=80,y=90)
but_pl=Button(root,bd=4,text="+",font=("Courier New",16,'bold'),bg="dark grey", command=btnAdd)
but_pl.place(x=120,y=90)
but4=Button(root,bd=4,text="4",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(4))
but4.place(x=0,y=140)
but5=Button(root,bd=4,text="5",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(5))
but5.place(x=40,y=140)
but6=Button(root,bd=4,text="6",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(6))
but6.place(x=80,y=140)
but_sub=Button(root,bd=4,text="-",font=("Courier New",16,'bold'),bg="dark grey", command=btnSub)
but_sub.place(x=120,y=140)
but7=Button(root,bd=4,text="7",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(7))
but7.place(x=0,y=190)
but8=Button(root,bd=4,text="8",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(8))
but8.place(x=40,y=190)
but9=Button(root,bd=4,text="9",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(9))
but9.place(x=80,y=190)
but_mul=Button(root,bd=4,text="*",font=("Courier New",16,'bold'),bg="dark grey", command=btnMul)
but_mul.place(x=120,y=190)
but0=Button(root,bd=4,text="0",font=("Courier New",16,'bold'),bg="white", command=lambda:btnClick(0))
but0.place(x=0,y=240)
but_pt=Button(root,bd=4,text=".",font=("Courier New",16,'bold'),bg="white", command=btnPoint)
but_pt.place(x=40,y=240)
but_eq=Button(root,bd=4,text="=",font=("Courier New",16,'bold'),bg="yellow", command=btnEqualsInput)
but_eq.place(x=80,y=240)
but_div=Button(root,bd=4,text="/",font=("Courier New",16,'bold'),bg="dark grey", command=btnDiv)
but_div.place(x=120,y=240)
root.mainloop()