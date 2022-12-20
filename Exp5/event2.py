from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def save():
   firstName = firstNameEntry.get()
   lastName = lastNameEntry.get()
   email = emailEntry.get()
   education = educationEntry.get()
   address = addressEntry.get()
   country = countryEntry.get()
   city = cityEntry.get()
   state = stateEntry.get()
   pincode = pincodeEntry.get()
   countryCode = countryCodeEntry.get()
   phoneNumber = phoneEntry.get()
   hobbies = hobbiesEntry.get()


   companyName = companyNameEntry.get()
   jobTitle = jobtitleEntry1 .get()
   here = hereEntry.get()


   referenceName = referenceNameEntry1.get()
   referencePhone = referencePhoneEntry1.get()


   referenceName2 = referenceNameEntry2.get()
   referencePhone2 = referencePhoneEntry2.get()

   fileName = firstName + lastName
   
   with open(fileName + ".txt","w") as f:
       f.write(f"FirstName: {firstName}\n")
       f.write(f"LastName : {lastName}\n")
       f.write(f"Email-Id : {email}\n")
       f.write(f"Education : {education}\n")
       f.write(f"Address : {address}\n")
       f.write(f"Country : {country}\n")
       f.write(f"City : {city}\n")
       f.write(f"State: {state}\n")
       f.write(f"Zip Code : {pincode}\n")
       f.write(f"Phone Number : {phoneNumber}\n")
       f.write(f"Hobbies : {hobbies}\n")
       f.write("Previous/Current Employment Details\n")
       f.write(f"Comapany Name: {companyName}\n")
       f.write(f"Job Title : {jobTitle}\n")
       f.write(f"Working Duration : {here}\n")
       f.write(f"Reference Name1 : {referenceName}\n")
       f.write(f"Reference Phone : {referencePhone}\n")
       f.write(f"Reference Name2 : {referenceName2}\n")
       f.write(f"Reference Phone2: {referencePhone2}\n")


master = Tk()
master.title("tk")
master.geometry("412x717")
Label(master, text="Name ").place(x=0, y=10)
Label(master, text="Email ").place(x=0, y=50)
Label(master, text="Education ").place(x=0, y=90)
Label(master, text="Resume ").place(x=0, y=130)
Label(master, text="Address").place(x=0, y=170)
Label(master, text="Phone Number ").place(x=0, y=290)
Label(master, text="What are your hobbies?").place(x=0, y=310)
Label(master, text="PREVIOUS/CURRENT EMPLOYMENT DETAILS").place(x=0, y=350)
Label(master, text="Comapany Name ").place(x=0, y=370)
Label(master, text="Job Title ").place(x=0, y=410)
Label(master, text="How long were you").place(x=0, y=430)
Label(master, text="here? ").place(x=0, y=450)
Label(master, text="REFERENCE #1").place(x=0, y=470)
Label(master, text="Name ").place(x=0, y=490)
Label(master, text="Phone ").place(x=0, y=530)
Label(master, text="REFERENCE #2 ").place(x=0, y=550)
Label(master, text="Name ").place(x=0, y=570)
Label(master, text="Phone ").place(x=0, y=610)
firstNameEntry = Entry(master, width=20)
firstNameEntry.place(x=120, y=10)
lastNameEntry = Entry(master, width=20)
lastNameEntry.place(x=260, y=10)


emailEntry = Entry(master, width=40)
emailEntry.place(x=120, y=50)

addressEntry = Entry(master, width=40)
addressEntry.place(x=120, y=130)


addressEntry2 = Entry(master, width=40).place(x=120, y=170)


cityEntry = Entry(master, width=18)
cityEntry.place(x=120, y=250)
cityEntry.insert(0,"City")


stateEntry = Entry(master, width=25)
stateEntry.place(x=240, y=250)
stateEntry.insert(0,"State")


pincodeEntry = Entry(master, width=10)
pincodeEntry.place(x=400, y=250)
pincodeEntry.insert(0,"PinCode")


phoneEntry = Entry(master, width=30)
phoneEntry.place(x=190, y=290)
phoneEntry.insert(0,"Phone Number")

countryCodeEntry = Entry(master, width=5)
countryCodeEntry.place(x=120, y=290)
countryCodeEntry.insert(0,"Code")


hobbiesEntry = Entry(master, width=60)
hobbiesEntry.place(x=0, y=330)


companyNameEntry = Entry(master, width=40)
companyNameEntry.place(x=120, y=370)


jobtitleEntry1 = Entry(master, width=40)
jobtitleEntry1.place(x=120, y=410)


hereEntry = Entry(master, width=40)
hereEntry.place(x=120, y=450)


referenceNameEntry1 = Entry(master, width=40)
referenceNameEntry1.place(x=120, y=490)


referencePhoneEntry1 = Entry(master, width=40)
referencePhoneEntry1.place(x=120, y=530)


referenceNameEntry2 = Entry(master, width=40)
referenceNameEntry2.place(x=120, y=570)

#jobTitleEntry2 = Entry(master, width=40).place(x=120, y=410)


referencePhoneEntry2 = Entry(master, width=40)
referencePhoneEntry2.place(x=120, y=610)


educationEntry = StringVar()
education = ttk.Combobox(master, width=35, textvariable=educationEntry)
education["values"] = (
    " X",
    " XII",
    "BTech",
    " BSc",
    " MBBS",
    " LLB",
    " MSc",
    " MTech",
)
education.place(x=120, y=90)
education.set("Please Choose")
countryEntry = StringVar()
country = ttk.Combobox(master, width=35, textvariable=countryEntry)
country["values"] = (
    " India",
    " USA",
    "Australia",
    " Canada",
    " Denmark",
    " Nepal",
    " Srilanka",
    " Brazil",
)
country.place(x=120, y=210)
country.set("Select a Country")
btn = Button(master, text="Apply",command=save).place(x=160, y=650)


mainloop()
