#1
from tkinter import*

root=Tk()

root.title('tk')
label_0=Label(root, text='Bookingid')
label_0.grid(row=0)
entry_0=Entry(root)
entry_0.grid(row=0,column=1)
label_1=Label(root, text='Passenger Name:')
label_1.grid(row=1)
entry_1=Entry(root)
entry_1.grid(row=1,column=1)
label_2=Label(root, text='Flight')
label_2.grid(row=2)
entry_2=Entry(root)
entry_2.insert(0,'IND345')
entry_2.grid(row=2,column=1)
label_2=Label(root, text='Source')
label_2.grid(row=3)
var_0=IntVar()
radio_0=Radiobutton(root, text='Delhi',value=1,variable=var_0)
radio_0.grid(row=3,column=1)
radio_1=Radiobutton(root, text='Mumbai',value=2,variable=var_0)
radio_1.grid(row=3,column=2)
label_3=Label(root, text='Destination')
label_3.grid(row=3,column=3)
radio_2=Radiobutton(root, text='Chennai',value=3, variable=var_0)
radio_2.grid(row=3,column=4)
radio_3=Radiobutton(root, text='Kolkata', value=4, variable=var_0)
radio_3.grid(row=3,column=5)
label_4=Label(root,text='Duration')
label_4.grid(row=4)
var_1=DoubleVar(value=3)
spin_0=Spinbox(root,from_=0, to=100, textvariable=var_1)
spin_0.grid(row=4, column=1)
bt_0=Button(root, text="Insert")
bt_0.grid(row=5)
bt_1=Button(root, text="Update")
bt_1.grid(row=5,column=1)
bt_2=Button(root, text="Delete")
bt_2.grid(row=6)
bt_3=Button(root, text="Select")
bt_3.grid(row=6,column=1)

root.mainloop()

