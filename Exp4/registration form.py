#8
from tkinter import *

root=Tk()

root.geometry('500x300')
root.configure(background='light green')
root.title('registration form')
label_0=Label(root, text='Form',bg='light green')
label_0.grid(row=0,column=1)
label_1=Label(root, text='Name', bg='light green')
label_1.grid(row=1)
entry_0=Entry(root, width=50)
entry_0.grid(row=1, column=1)
label_2=Label(root, text='Course', bg='light green')
label_2.grid(row=2)
entry_1=Entry(root, width=50)
entry_1.grid(row=2, column=1)
label_3=Label(root, text='Semester', bg='light green')
label_3.grid(row=3)
entry_2=Entry(root, width=50)
entry_2.grid(row=3,column=1)
label_4=Label(root, text='Form No.', bg='light green')
label_4.grid(row=4)
entry_3=Entry(root, width=50)
entry_3.grid(row=4, column=1)
label_5=Label(root, text='Contact No.', bg='light green')
label_5.grid(row=5)
entry_4=Entry(root, width=50)
entry_4.grid(row=5, column=1)
label_6=Label(root, text='Email id', bg='light green')
label_6.grid(row=6)
entry_5=Entry(root, width=50)
entry_5.grid(row=6, column=1)
label_7=Label(root, text='Address', bg='light green')
label_7.grid(row=7)
entry_6=Entry(root, width=50)
entry_6.grid(row=7, column=1)

bt_0=Button(root, text='Submit',bg='red')
bt_0.grid(row=8,column=1)

root.mainloop()