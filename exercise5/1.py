
from tkinter import *
from tkinter import messagebox
from tkinter.tix import COLUMN
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
master = Tk()
master.configure(bg='#8533ff')
master.title('tk')
master.geometry('1000x5000')
Label(master,bg='#8533ff',fg='white', text='First Name ').grid(row=0)
Label(master,bg='#8533ff', fg='white',text='(max 30 chracters a-z and AZ)').grid(row=0,column=2)

Label(master, bg='#8533ff',fg='white',text='Last Name').grid(row=1)

Label(master, bg='#8533ff',fg='white',text='(max 30 chracters a-z and AZ)').grid(row=1,column=2)
Label(master, bg='#8533ff',fg='white',text='Date of birth').grid(row=2)
Label(master,bg='#8533ff', fg='white',text='Email ID  ').grid(row=3)
Label(master,bg='#8533ff', fg='white',text='Mobile Number').grid(row=4)
Label(master,bg='#8533ff', fg='white',text='(10 digit number)').grid(row=4,column=2)
Label(master,bg='#8533ff', fg='white',text='Gender    ').grid(row=5)
Label(master,bg='#8533ff', fg='white',text='Address   ').grid(row=6)
Label(master,bg='#8533ff', fg='white',text='City  ').grid(row=7)
Label(master,bg='#8533ff', fg='white',text='(max 30 chracters a-z and AZ)').grid(row=7,column=2)

Label(master,bg='#8533ff',fg='white',text='Pincode').grid(row=8)

Label(master,bg='#8533ff',fg='white',text='(6 digit number)').grid(row=8,column=2)

Label(master,bg='#8533ff',fg='white',text='State').grid(row=9)

Label(master,bg='#8533ff',fg='white',text='(max 30 chracters a-z and AZ)').grid(row=9,column=2)

Label(master,bg='#8533ff',fg='white',text='Country').grid(row=10)

Label(master,bg='#8533ff',fg='white',text='Hobbies').grid(row=11)

Label(master,bg='#8533ff',fg='white',text='Qualification)').grid(row=12)

Label(master,bg='#8533ff',fg='white',text='Sl.No').grid(row=12,column=1)

Label(master,bg='#8533ff',fg='white',text='Examination').grid(row=12,column=2)

Label(master,bg='#8533ff',fg='white',text='Board').grid(row=12,column=3)

Label(master,bg='#8533ff',fg='white',text='Percentage').grid(row=12,column=4)

Label(master,bg='#8533ff',fg='white',text='YearofPassing').grid(row=12,column=5)

Label(master,bg='#8533ff',fg='white',text='1').grid(row=13,column=1)
Label(master,bg='#8533ff',fg='white', text='2').grid(row=14,column=1)
Label(master,bg='#8533ff',fg='white', text='3').grid(row=15,column=1)
Label(master,bg='#8533ff',fg='white', text='4').grid(row=16,column=1)
Label(master, bg='#8533ff',fg='white',text='Class X').grid(row=13,column=2)
Label(master,bg='#8533ff', fg='white',text='Class XII').grid(row=14,column=2)
Label(master,bg='#8533ff',fg='white',text='Graduation').grid(row=15,column=2)
Label(master,bg='#8533ff',fg='white', text='Masters').grid(row=16,column=2)
# Label(master, text= "Day:").grid(row=2,column=1)

Label(master,bg='#8533ff',fg='white', text='Courses   Applied').grid(row=17)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e13= Entry(master)
e14= Entry(master)
e15= Entry(master)
e16= Entry(master)
e17= Entry(master)
e18= Entry(master)
e19= Entry(master) 
e20= Entry(master)
e21= Entry(master)
e22= Entry(master)
e23= Entry(master)
e24= Entry(master)
e1.grid(row=0, column=1,ipadx=30)
e2.grid(row=1, column=1,ipadx=30)
e3.grid(row=3,column=1,ipadx=30)
e4.grid(row=4,column=1,ipadx=30)
e5.grid(row=6,column=1,ipadx=30,ipady=30)
e6.grid(row=7,column=1,ipadx=30)
e7.grid(row=8,column=1,ipadx=30)
e8.grid(row=9,column=1,ipadx=30)
e9.grid(row=10,column=1,ipadx=30)
e13.grid(row=13,column=3,ipadx=30)
e14.grid(row=14,column=3,ipadx=30)
e15.grid(row=15,column=3,ipadx=30)
e16.grid(row=16,column=3,ipadx=30)
e17.grid(row=13,column=4,ipadx=30)
e18.grid(row=14,column=4,ipadx=30)
e19.grid(row=15,column=4,ipadx=30)
e20.grid(row=16,column=4,ipadx=30)
e21.grid(row=13,column=5,ipadx=30)
e22.grid(row=14,column=5,ipadx=30)
e23.grid(row=15,column=5,ipadx=30)
e24.grid(row=16,column=5,ipadx=30) 
var1 = IntVar()
Radiobutton(master,bg='#8533ff', fg='white',text="Male",variable=var1).grid(row=5, column=1, sticky=W,ipady=10,ipadx=30)
var2 = IntVar()
Radiobutton(master,bg='#8533ff',fg='white',text="Female", variable=var2).grid(row=5, column=2, sticky=W,ipady=10,ipadx=10)
var3 = IntVar()
Checkbutton(master,bg='#8533ff',fg='white', text="Drawing",variable=var3).grid(row=11, column=1,sticky=W,ipady=10,ipadx=30)
var4 = IntVar()
Checkbutton(master,bg='#8533ff', fg='white',text="Singing",variable=var4).grid(row=11, column=2, sticky=W,ipady=10,ipadx=10)
var5 = IntVar()
Checkbutton(master,bg='#8533ff',fg='white',text="Dancing",variable=var5).grid(row=11, column=3, sticky=W,ipady=10,ipadx=30)
var6 = IntVar()
Checkbutton(master,bg='#8533ff',fg='white', text="Sketching",variable=var6).grid(row=11, column=4, sticky=W,ipady=10,ipadx=10)
var7 = IntVar()
Radiobutton(master,bg='#8533ff',fg='white',text="BCA",variable=var7).grid(row=17, column=1,sticky=W,ipady=10,ipadx=30)
var8 = IntVar()
Radiobutton(master, bg='#8533ff',fg='white',text="B.Com",variable=var8).grid(row=17, column=2, sticky=W,ipady=10,ipadx=10)
var9 = IntVar() 
Radiobutton(master,bg='#8533ff',fg='white',text="B.Sc",variable=var9).grid(row=17, column=3,sticky=W,ipady=10,ipadx=30) 
var10 = IntVar()
Radiobutton(master,bg='#8533ff', fg='white',text="B.A",variable=var10).grid(row=17, column=4, sticky=W,ipady=10,ipadx=10)
n = tk.StringVar()
p = tk.StringVar()
q = tk.StringVar()
monthchoosen = ttk.Combobox(master, width = 27, textvariable = n)
datechosen = ttk.Combobox(master, width = 27, textvariable = p)
yearchosen = ttk.Combobox(master, width = 27, textvariable = q)
datechosen['values']=("1",
                      "2",
                      "3",
                      "4",
                      "5")
monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October', 
                          ' November',
                          ' December')
yearchosen['values']=("2001",
                      "2002",
                      "2003",
                      "2004")
datechosen.grid(column=1,row=2)
datechosen.set("Date")
monthchoosen.grid(column = 2, row = 2)
monthchoosen.set("Month")
yearchosen.grid(column = 3, row = 2)
yearchosen.set("Year")
btn = Button(master, text='Submit').grid(row=18,column=2)
btn = Button(master, text='Reset').grid(row=18, column=3)
master.mainloop()