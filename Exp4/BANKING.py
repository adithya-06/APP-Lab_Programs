#2
from tkinter import*

root=Tk()

#root.geometry('320x250')
root.title('tk')
label_0=Label(root, text='Custid')
label_0.grid(row=0)
entry_0=Entry(root)
entry_0.grid(row=0,column=1)
label_1=Label(root, text='Customer Name:')
label_1.grid(row=1)
entry_1=Entry(root)
entry_1.grid(row=1,column=1)
label_2=Label(root, text='Branch')
label_2.grid(row=2)
entry_2=Entry(root)
entry_2.insert(0,'adyar')
entry_2.grid(row=2,column=1)
label_3=Label(root, text='account type')
label_3.grid(row=3)
var_0=IntVar()
radio_0=Radiobutton(root, text='Saving', value=1, variable=var_0)
radio_0.grid(row=3,column=1)
radio_1=Radiobutton(root, text='Non Saving', value=2, variable=var_0)
radio_1.grid(row=3,column=2)
label_4=Label(root, text='Amount')
label_4.grid(row=4)
scale_0=Scale(root, from_=19, to=100,orient=HORIZONTAL)
scale_0.grid(row=4, column=1)
bt_0=Button(root, text="Insert")
bt_0.grid(row=5)
bt_1=Button(root, text="Update")
bt_1.grid(row=5,column=1)
bt_2=Button(root, text="Delete")
bt_2.grid(row=6)
bt_3=Button(root, text="Select")
bt_3.grid(row=6,column=1)

root.mainloop()