from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
master = Tk()
master.title('tk')
master.geometry('800x800')
Label(master,text='Title ').grid(row=0)
Label(master, text='Last Name ').grid(row=1)
Label(master,text='First Name ').grid(row=2)
Label(master, text='Share with ').grid(row=3)
Label(master,text='Business number ').grid(row=4)
Label(master, text='Mobile Number ').grid(row=5)
Label(master, text='Email Address ').grid(row=6)
Label(master, text='Date of Arrival ').grid(row=7)
Label(master,text='Date of Departure ').grid(row=8)
Label(master, text='Name on Credit Number ').grid(row=9)
Label(master,text='Credit Card Number ').grid(row=10)
Label(master, text='Expire Date ').grid(row=11)
Label(master,text='CVV Number ').grid(row=12)
Label(master,text='Payment ').grid(row=13)

for i in range(0,14):
    ei= Entry(master, width=50).grid(row=i,column=1)
var1 = IntVar() 
Checkbutton(master, text="Credit Card",variable=var1).grid(row=13, column=1, sticky=W,ipady=10, ipadx=10) 
var2 = IntVar()
Checkbutton(master,text="Direct bank Transfer", variable=var2).grid(row=13,column=2, sticky=W,ipady=10,ipadx=10)
Label(master,font=("Arial", 10), text= 'Negotiated Rates: ').grid(row=14,column=0)
var3 = IntVar()
Checkbutton(master,text="Deluxe Room Single ", variable=var3).grid(row=15,column=0, sticky=W,ipady=10,ipadx=10)
Label(master,text='R 1700 ').grid(row=15,column=1)
var4 = IntVar()
Checkbutton(master,text="Deluxe Room Double ", variable=var4).grid(row=15,column=2, sticky=W,ipady=10,ipadx=10)
Label(master,text='R 1700 ').grid(row=15,column=3)
var5 = IntVar()
Checkbutton(master,text="Suites Room Single ", variable=var5).grid(row=16,column=0, sticky=W,ipady=10,ipadx=10)
Label(master,text='R 1700 ').grid(row=16,column=1)
var6 = IntVar()
Checkbutton(master,text="Suites Room Double ", variable=var6).grid(row=16,column=2, sticky=W,ipady=10,ipadx=10)
Label(master,text='R 1700 ').grid(row=16,column=3)
Label(master,font=("Arial", 10), text= 'Room Preference: ').grid(row=17,column=0)
var7 = IntVar()
Checkbutton(master,text="King Bed ", variable=var7).grid(row=18, column=0,
sticky=W,ipady=10,ipadx=10)
var8 = IntVar() 
Checkbutton(master,text="Twin-Two Single Beds ",variable=var8).grid(row=18, column=2, sticky=W,ipady=10,ipadx=10) 
Label(master,font=("Arial", 10), text= 'The above rates are quoted per room, per night. The rates includes breakfast, 14% vat, and Excludes 1% Tourism Levy ').place(x=0,y=500) 
Label(master,font=("Arial", 10), text= 'and a voluntary R10 donation to the Ambela Community Trust that will be levies onto your account.').place(x=0,y=525) 
Label(master,font=("Arial", 10), text= 'Credit Card will be changed on receipt of this form and details will also be used to settle all incidentals ').place(x=0,y=550) 
Label(master,font=("Arial", 10), text= 'not settle on departure. A copy of the final folio will be sent to you should there be any unsettled changes.').place(x=0,y=575) 
Label(master,font=("Arial", 10), text= 'In order to qualify for the above rates your booking needs to be made on or before 15th January 2016').place(x=0,y=600) 
Label(master,font=("Arial", 10), text= 'Terms and conditions can be found on the next page').place(x=0,y=625) 
Label(master,font=("Arial", 10), text= 'The rate is valid for seven days before and after the conference dates. Check in time is 14:00 & check out time is 11:00').place(x=0,y=650) 
Label(master,font=("Arial", 10), text= 'By your signature hereto, you are accepting all terms and conditions specified on this form and confirm that all information').place(x=0,y=675) 
Label(master,font=("Arial", 10), text= 'given is current and accurate.').place(x=0,y=700) 
Label(master,font=("Arial", 10), text='Signature___________________').place(x=0,y=740) 
Label(master,font=("Arial", 10), text='Pointname___________________').place(x=400,y=740) 
Label(master,font=("Arial", 10), text='Date________________________').place(x=0,y=765) 
master.mainloop()
