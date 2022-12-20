import tkinter as tk


def save():
    file_name = firstNameEntry.get() + lastNameEntry.get()

    first_Name = firstNameEntry.get()
    last_Name = lastNameEntry.get()

    day = dayValue.get()
    month = monthValue.get()
    year = yearValue.get()
    gender = "Female"
    if genderValue.get():
        gender = "Male"
    mailId = mailIdEntry.get()
    mobileNumber = mobileNumberEntry.get()
    address = addressEntry.get()
    city = cityEntry.get()
    pincode = pincodeEntry.get()
    state = stateEntry.get()
    country = countryEntry.get()
    hobbies = "singing"
    temp_hobbies = hobbiesEntry.get()
    if temp_hobbies == 1:
        hobbies = "singing"
    elif temp_hobbies == 2:
        hobbies = "dancing"
    elif temp_hobbies == 3:
        hobbies = "sketching"
    elif temp_hobbies == 4:
        hobbies = othersEntry.get()

    classXPercentage = classXEntry.get()
    classX_YOP = classXYOP.get()
    classXIIPercentage = classXIIEntry.get()
    classXII_YOP = classXIIYOP.get()
    graduationPercentage = graduationEntry.get()
    graduation_YOP = graduationYOP.get()
    masters = mastersEntry.get()
    masters_YOP = mastersYOP.get()

    coursesApplied = ""
    temp_coursedApplied = degree.get()

    if temp_coursedApplied == 1:
        coursesApplied = "B.A"
    elif temp_coursedApplied == 2:
        coursesApplied = "B.com"
    else:
        coursesApplied = "B.Sc"

    with open(file_name + ".txt", "w") as file_object:
        file_object.write(f"First Name: {first_Name}\n")
        file_object.write(f"last Name: {last_Name}\n")
        file_object.write(f"Date of Birth: {day} - {month} - {year}\n")
        file_object.write(f"Email-Id: {mailId}\n")
        file_object.write(f"Mobile Number: {mobileNumber}\n")
        file_object.write(f"Gender: {gender}\n")
        file_object.write(f"Address: {address}\n")
        file_object.write(f"City: {city}\n")
        file_object.write(f"PinCode: {pincode}\n")
        file_object.write(f"State: {state}\n")
        file_object.write(f"Country: {country}\n")
        file_object.write(f"Hobbies: {hobbies}\n")
        file_object.write(f"Class X percentage : {classXPercentage}\t")
        file_object.write(f"Year Of Passing: {classX_YOP}\n")
        file_object.write(f"Class XII percentage: {classXIIPercentage}\t")
        file_object.write(f"Year Of Passing: {classXII_YOP}\n")
        file_object.write(f"Graduation percentage: {graduationPercentage}\t")
        file_object.write(f"Year Of Passing: {graduation_YOP}\n")
        file_object.write(f"Masters: {masters}\t")
        file_object.write(f"Year Of Passing: {masters_YOP}\n")
        file_object.write(f"Courses Applied: {coursesApplied}\n")


def reset_data():
    firstNameEntry.delete(first=0, last=len(firstNameEntry.get()))
    lastNameEntry.delete(first=0, last=len(lastNameEntry.get()))
    dayValue.set("Day")
    monthValue.set("Month")
    yearValue.set("Year")
    genderValue.set(0)
    mailIdEntry.delete(first=0, last=len(mailIdEntry.get()))
    mobileNumberEntry.delete(first=0, last=len(mobileNumberEntry.get()))
    stateEntry.delete(first=0, last=len(stateEntry.get()))
    countryEntry.delete(first=0, last=len(countryEntry.get()))
    pincodeEntry.delete(first=0, last=len(pincodeEntry.get()))

    addressEntry.delete(first=0, last=len(addressEntry.get()))
    cityEntry.delete(first=0, last=len(cityEntry.get()))
    genderValue.set(0)
    pincodeEntry.delete(first=0, last=len(addressEntry.get()))
    stateEntry.delete(first=0, last=len(addressEntry.get()))
    countryEntry.delete(first=0, last=len(addressEntry.get()))
    othersEntry.delete(first=0, last=len(othersEntry.get()))
    classXEntry.delete(first=0, last=len(classXYOP.get()))
    classXYOP.delete(first=0, last=len(classXYOP.get()))

    classXIIEntry.delete(first=0, last=len(classXIIEntry.get()))
    classXIIYOP.delete(first=0, last=len(classXIIYOP.get()))

    graduationEntry.delete(first=0, last=len(graduationEntry.get()))
    graduationYOP.delete(first=0, last=len(graduationYOP.get()))

    mastersEntry.delete(first=0, last=len(mastersEntry.get()))
    mastersYOP.delete(first=0, last=len(mastersYOP.get()))


root = tk.Tk()
#root.geometry("1000x800")
root.configure(background='dark blue')
firstName = tk.Label(root, text="First Name")
firstName.grid(row=0)
firstNameEntry = tk.Entry(root)
firstNameEntry.grid(row=0, column=1)
lastName = tk.Label(root, text="Last Name")
lastName.grid(row=1)
lastNameEntry = tk.Entry(root)
lastNameEntry.grid(row=1, column=1)
dateOfBirth = tk.Label(root, text="Date of Birth")
dateOfBirth.grid(row=3, column=0)
dayValue = tk.StringVar(root)
dayValue.set("Day")
date = ["1", "2", "3", "4", "5"]
dayOptionMenu = tk.OptionMenu(root, dayValue, *date).grid(row=3, column=1)
monthValue = tk.StringVar(root)
monthValue.set("Month")
month = ["1", "2", "3", "4", "5"]
monthOptionMenu = tk.OptionMenu(root, monthValue, *month).grid(row=3, column=2)
yearValue = tk.StringVar(root)
yearValue.set("Year")
year = ["1", "2", "3", "4", "5"]
yearOptionMenu = tk.OptionMenu(root, yearValue, *year).grid(row=3, column=3)
mailId = tk.Label(root, text="EMAIL ID")
mailId.grid(row=4)
mailIdEntry = tk.Entry(root)
mailIdEntry.grid(row=4, column=1)
mobileNumber = tk.Label(root, text="MOBILE NUMBER")
mobileNumber.grid(row=5)
mobileNumberEntry = tk.Entry(root)
mobileNumberEntry.grid(row=5, column=1)
gender = tk.Label(root, text="Gender")
gender.grid(row=6, column=0)
genderValue = tk.IntVar()
male = tk.Radiobutton(root, text="Male", variable=genderValue, value=1).grid(
    row=6, column=1
)
female = tk.Radiobutton(root, text="Female", variable=genderValue, value=0).grid(
    row=6, column=2
)
address = tk.Label(root, text="ADDRESS")
address.grid(row=7)
addressEntry = tk.Entry(root)
addressEntry.grid(row=7, column=1)
city = tk.Label(root, text="CITY")
city.grid(row=8)
cityEntry = tk.Entry(root)
cityEntry.grid(row=8, column=1)
pincode = tk.Label(root, text="PIN CODE")
pincode.grid(row=9)
pincodeEntry = tk.Entry(root)
pincodeEntry.grid(row=9, column=1)
state = tk.Label(root, text="STATE")
state.grid(row=10)
stateEntry = tk.Entry(root)
stateEntry.grid(row=10, column=1)
country = tk.Label(root, text="COUNTRY")
country.grid(row=11)
countryEntry = tk.Entry(root)
countryEntry.grid(row=11, column=1)
hobbies = tk.Label(root, text="HOBBIES")
hobbies.grid(row=12, column=0)
hobbiesEntry = tk.IntVar()
singing = tk.Radiobutton(root, text="singing", variable=hobbiesEntry, value=1).grid(
    row=12, column=1
)
dancing = tk.Radiobutton(root, text="dancing", variable=hobbiesEntry, value=2).grid(
    row=12, column=2
)
sketching = tk.Radiobutton(root, text="sketching", variable=hobbiesEntry, value=3).grid(
    row=12, column=3
)
others = tk.Radiobutton(root, text="others", variable=hobbiesEntry, value=4).grid(
    row=13, column=1
)
othersEntry = tk.Entry(root)
othersEntry.grid(row=13, column=2)
qualification = tk.Label(root, text="QUALIFICATION")
qualification.grid(row=14, column=0)
si_no = tk.Label(root, text="SI.NO.")
si_no.grid(row=14, column=1)
board = tk.Label(root, text="BOARD")
board.grid(row=14, column=2)
percentage = tk.Label(root, text="PERCENTAGE")
percentage.grid(row=14, column=3)
yearOfPassing = tk.Label(root, text="YEAR OF PASSING")
yearOfPassing.grid(row=14, column=4)
si_no1 = tk.Label(root, text="1")
si_no1.grid(row=15, column=1)
si_no2 = tk.Label(root, text="2")
si_no2.grid(row=16, column=1)
si_no3 = tk.Label(root, text="3")
si_no3.grid(row=17, column=1)
si_no4 = tk.Label(root, text="4")
si_no4.grid(row=18, column=1)
classX = tk.Label(root, text="CLASS X")
classX.grid(row=15, column=2)
classXII = tk.Label(root, text="CLASS XII")
classXII.grid(row=16, column=2)
graduation = tk.Label(root, text="GRADUATION")
graduation.grid(row=17, column=2)
masters = tk.Label(root, text="MASTERS")
masters.grid(row=18, column=2)
classXEntry = tk.Entry(root)
classXEntry.grid(row=15, column=3)
classXIIEntry = tk.Entry(root)
classXIIEntry.grid(row=16, column=3)
graduationEntry = tk.Entry(root)
graduationEntry.grid(row=17, column=3)
mastersEntry = tk.Entry(root)
mastersEntry.grid(row=18, column=3)
classXYOP = tk.Entry(root)
classXYOP.grid(row=15, column=4)
classXIIYOP = tk.Entry(root)
classXIIYOP.grid(row=16, column=4)
graduationYOP = tk.Entry(root)
graduationYOP.grid(row=17, column=4)
mastersYOP = tk.Entry(root)
mastersYOP.grid(row=18, column=4)
l4 = tk.Label(root, text="COURSES APPLIED")
l4.grid(row=19, column=0)
degree = tk.IntVar()
e5 = tk.Radiobutton(root, text="BCA", variable=degree, value=1).grid(row=20, column=1)
e6 = tk.Radiobutton(root, text="B.Com", variable=degree, value=2).grid(row=20, column=2)
e5 = tk.Radiobutton(root, text="B.Sc", variable=degree, value=3).grid(row=20, column=3)
e6 = tk.Radiobutton(root, text="B.A", variable=degree, value=4).grid(row=20, column=1)

submit = tk.Button(root, text="Submit", command=save).grid(row=24, column=2)
reset = tk.Button(root, text="Reset", command=reset_data).grid(row=24, column=3)
root.mainloop()
