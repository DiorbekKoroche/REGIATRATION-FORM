from tkinter import *
root = Tk()
root.geometry("400x200")

def getvals():
    print("Accepted")

# Heading
Label(root, text="REGIATRATION FORM", font="arial 15 bold").grid(row=0, column=4)

# Field Name
name = Label(root, text="Name", font="arial 10 bold")
phone = Label(root, text="Phone Number", font="arial 10 bold")
gender = Label(root, text="Gender", font="arial 10 bold")
emergency = Label(root, text="Emergency", font="arial 10 bold")
paymentmood = Label(root, text="Payment Mood", font="arial 10 bold")

# Packing Fields
name.grid(row=1, column=3)
phone.grid(row=2, column=3)
gender.grid(row=3, column=3)
emergency.grid(row=4, column=3)
paymentmood.grid(row=5, column=3)

# Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

# Cheating entry field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
emergencyentry = Entry(root, textvariable =emergencyvalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)

# Packing entry fields
nameentry.grid(row=1, column=4)
phoneentry.grid(row=2, column=4)
genderentry.grid(row=3, column=4)
emergencyentry.grid(row=4, column=4)
paymentmoodentry.grid(row=5, column=4)

# Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=4)

# Submit button
Button(text="Submit", command=getvals).grid(row=7, column=4)

root.mainloop()