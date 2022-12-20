from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.title('SET 3')
window.geometry('1000x1000')
l4 = Label(window, text="REGISTRATION INFORMATION",height=5).grid(row=0, columnspan=5)
Reg_period = Label(window, text="Registration period:(check one)").grid(row=1, column=0)
CheckVar1 = IntVar() 
C1 = Checkbutton(window, text = "One year", variable = CheckVar1, onvalue =1, offvalue = 0, width = 10).grid(row=1, column=1) 
C1 = Checkbutton(window, text = "Two years ($2 discount applies)", variable =CheckVar1, onvalue = 1, offvalue = 0, width = 25).grid(row=1, column=2) 
C1 = Checkbutton(window, text = "Three years ($3 discount applies)", variable= CheckVar1, onvalue = 1, offvalue = 0, width = 25).grid(row=1, column=3) 

Reg_type = Label(window, text="Registration type:(check one)").grid(row=2,column=0)
CheckVar1 = IntVar()
C1 = Checkbutton(window, text = "Original", variable = CheckVar1, onvalue = 1,offvalue = 0, height=2, width = 10).grid(row=2, column=1)
C1 = Checkbutton(window, text = "Renewal", variable = CheckVar1, onvalue =1, offvalue = 0, height=2, width = 10).grid(row=2, column=2)
C1 = Checkbutton(window, text = "Private", variable = CheckVar1, onvalue = 1,offvalue = 0, height=2, width = 10).grid(row=2, column=3)
C1 = Checkbutton(window, text = "Reissue (Plates & Decals)", variable =CheckVar1, onvalue = 1, offvalue = 0, height=2, width = 20).grid(row=2,column=4)

CheckVar1 = IntVar()
C1 = Checkbutton(window, text = "Reissue (Decals only)", variable = CheckVar1, onvalue = 1, offvalue = 0, width = 18).grid(row=3, column=0)
C1 = Checkbutton(window, text = "Rental Vehicle", variable = CheckVar1,onvalue = 1, offvalue = 0, width = 13).grid(row=3, column=1)
C1 = Checkbutton(window, text = "Transfer Liscence plate no.", variable = CheckVar1, onvalue = 1, offvalue = 0, width = 22).grid(row=3, column=2)
e1=Entry(window).grid(row=2,column=3)
l1 = Label(window, text="See reissue plates below \n under plates information ").grid(row=4, column=4) 

C1 = Checkbutton(window, text = "For Hire (complete 'For Hire \n information' section)", variable = CheckVar1, width = 30).grid(row=4, columnspan=2) 
C1 = Checkbutton(window, text = "Ridesharing (vanpool)(cannot exceed 16 passengers including driver.) ", variable = CheckVar1, width = 55).grid(row=4, columnspan=6)
l1=Label(window, text="seating \n capacity").grid(row=3, column=4)
e1=Entry(window, width=5).grid(row=3,column=5)

C1 = Checkbutton(window, text = "Amateur Radio Operator Call \n Letters - specify letters", variable = CheckVar1, width = 22).grid(row=5, columnspan=1)
e1=Entry(window, width=10).grid(row=4,column=1)

C1 = Checkbutton(window, text = "Other (specify)", variable = CheckVar1, onvalue = 1, offvalue = 0, width = 20).grid(row=5, column=1)
e1=Entry(window, width=10).grid(row=4,column=2)

l4 = Label(window, text="OWNER INFORMATION", height=5).grid(row=6, columnspan=5)
l5 = Label(window, text="OWNER FULL LEGAL NAME OR BUSINESS NAME(if business owned)").grid(row=7, column=1)
e1=Entry(window, width=45).grid(row=8,column=1)
l5 = Label(window, text="TELEPHONE NUMBER").grid(row=7, column=2)
e1=Entry(window, width=20).grid(row=8,column=2)
l5 = Label(window, text="DMV CUSTOMER NUMBER / FEIN / SSN").grid(row=7, column=3)
e1=Entry(window, width=30).grid(row=8,column=3)
 
l5 = Label(window, text="OWNER FULL LEGAL NAME OR BUSINESS NAME(if business owned)").grid(row=9, column=1) 
e1=Entry(window, width=45).grid(row=10,column=1)
l5 = Label(window, text="TELEPHONE NUMBER").grid(row=9, column=2)
e1=Entry(window, width=20).grid(row=10,column=2)
l5 = Label(window, text="DMV CUSTOMER NUMBER / FEIN / SSN").grid(row=9, column=3)
e1=Entry(window, width=30).grid(row=10,column=3)

l6 = Label(window, text = "Owners must provide their residence/ home/ business \n address where requested, this address cannot be a P.O.Box \n your must complete ISD form if you would like your address updated").grid(row=11, column=1)
l7=Label(window, text = "RESIDENCE/ BUSINESS JURISDICTION").grid(row=11, column=2)
e=Entry(window).grid(row=11, column=3)


l5 = Label(window, text="OWNER's RESIDENCE/ HOME/ BUSINESS ADDRESS").grid(row=12, column=1)
e1=Entry(window, width=45).grid(row=13,column=1)
l5 = Label(window, text="CITY").grid(row=12, column=2)
e1=Entry(window, width=20).grid(row=13,column=2)
l5 = Label(window, text="ZIP CODE").grid(row=12, column=3)
e1=Entry(window, width=15).grid(row=13,column=3)

l5 = Label(window, text="CO-OWNER's RESIDENCE/ HOME/ BUSINESS ADDRESS").grid(row=14, column=1)
e1=Entry(window, width=45).grid(row=15,column=1) 
l5 = Label(window, text="CITY").grid(row=14, column=2)
e1=Entry(window, width=20).grid(row=15,column=2)
l5 = Label(window, text="ZIP CODE").grid(row=14, column=3)
e1=Entry(window, width=15).grid(row=15,column=3)

l5 = Label(window, text="OWNER EMAIL ADDRESS").grid(row=16, column=1)
e1=Entry(window, width=20).grid(row=17,column=1)
l5 = Label(window, text="CO-OWNER EMAIL ADDRESS").grid(row=16,column=2)
e1=Entry(window, width=20).grid(row=17,column=2)


window.mainloop()