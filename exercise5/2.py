from tkinter import *
from tkinter import messagebox
from tkinter import ttk
master = Tk()
master.title('tk')
master.geometry('600x800')

Label(master,font=("Arial", 15), text= 'Job Application').place(x=5+120,y= 0)
Label(master, text= 'Personal Information').place(x=5,y= 5+ 10)
Label(master, text= 'Name ').place(x=5+0,y= 25+ 15+10)
Label(master, text='Email ').place(x=5+0,y= 25+ 15+50)
Label(master, text='Education ').place(x=5+0,y= 25+ 15+90)
Label(master, text='Resume ').place(x=5+0,y= 25+ 15+130)
Label(master, text='Address').place(x=5+0,y= 25+ 15+170)
Label(master, text='Phone Number ').place(x=5+0,y= 25+ 15+290)
Label(master, text='What are your hobbies?').place(x=5+0,y= 25+ 15+310)
Label(master,text='PREVIOUS/CURRENT EMPLOYMENT DETAILS').place(x=5+0,y= 25+ 15+350)
Label(master, text='Comapany Name ').place(x=5+0,y= 25+ 15+370)
Label(master, text='Job Title ').place(x=5+0,y= 25+ 15+410)
Label(master, text='How long were you').place(x=5+0,y= 25+ 15+430)
Label(master, text='here? ').place(x=5+0,y= 25+ 15+450)
Label(master, text='REFERENCE #1').place(x=5+0,y= 25+ 15+470)
Label(master, text='Name ').place(x=5+0,y= 25+ 15+490) 
Label(master, text='Phone ').place(x=5+0,y= 25+ 15+530)
Label(master, text='REFERENCE #2 ').place(x=5+0,y= 25+ 15+550)
Label(master, text='Name ').place(x=5+0,y= 25+ 15+570)
Label(master, text='Phone ').place(x=5+0,y= 25+ 15+610)
e1 = Entry(master,width=20).place(x=5+120,y= 25+ 15+10)
e18=Entry(master,width=20).place(x=5+260,y= 25+ 15+10)
e2 = Entry(master,width=40).place(x=5+120,y= 25+ 15+50)
e4 = Entry(master,width=40).place(x=5+120,y= 25+ 15+130)
e5=Entry(master,width=40).place(x=5+120,y= 25+ 15+170)
e6=Entry(master,width=18).place(x=5+120,y= 25+ 15+250)
e19=Entry(master,width=5).place(x=5+240,y= 25+ 15+250)
e20=Entry(master,width=10).place(x=5+280,y= 25+ 15+250)
e8=Entry(master,width=30).place(x=5+160,y= 25+ 15+290)
e21=Entry(master,width=5).place(x=5+120,y= 25+ 15+290)
e9 =Entry(master,width=60).place(x=5+0,y= 25+ 15+330)
e10=Entry(master,width=40).place(x=5+120,y= 25+ 15+370)
e11=Entry(master,width=40).place(x=5+120,y= 25+ 15+410)
e12=Entry(master,width=40).place(x=5+120,y= 25+ 15+450)
e13=Entry(master,width=40).place(x=5+120,y= 25+ 15+490)
e14=Entry(master,width=40).place(x=5+120,y= 25+ 15+530)
e15=Entry(master,width=40).place(x=5+120,y= 25+ 15+570)
e16=Entry(master,width=40).place(x=5+120,y= 25+ 15+410)
e17=Entry(master,width=40).place(x=5+120,y= 25+ 15+610)
n = StringVar()
monthchoosen = ttk.Combobox(master, text='Please Choose',width = 35,
textvariable = n)
monthchoosen['values'] = (' X',  
                          ' XII',
                          'BTech',
                          ' BSc',
                          ' MBBS',
                          ' LLB',
                          ' MSc',
                          ' MTech')
monthchoosen.place(x=5+120,y= 25+ 15+90)
monthchoosen.set('Please Choose')
p = StringVar()
countrychoosen= ttk.Combobox(master, text='Please Choose',width = 35,
textvariable = p)
countrychoosen['values'] = (' India', 
                          ' USA',
                          'Australia',
                          ' Canada',
                          ' Denmark',
                          ' Nepal',
                          ' Srilanka',
                          ' Brazil')
countrychoosen.place(x=5+120,y= 25+ 15+210)
countrychoosen.set('Select a Country')
btn = Button(master, text='Apply').place(x=5+160,y= 25+ 15+650)
master.mainloop()
