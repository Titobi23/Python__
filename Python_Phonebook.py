# Creating a Phone Directory
# Basically a phonebook

import csv

def menu():
    print("A) Add to Directory")
    print("B) Display Directory")
    print("X) Exit Directory Program")
    selection = input("--")
    if selection == "A":
        addToDirectory()
    elif selection == "B":
        displayDirectory()
    elif selection == "X":
        quit()
    else:
        print("Invalid Selection.")
        menu()

def addToDirectory():
    print("Add to Directory")
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    directory = open("Directory.csv", "a")
    outstring = firstName + "," + lastName + "," + email + "," + phone + "\n"
    directory.write(outstring)
    directory.close()
    print(firstName + " " + lastName + " added to directory. ")
    menu()

def displayDirectory():
    print("Display Directory")
    directory = open("Directory.csv", "r")
    try:
        rowtext = ""
        reader = csv.reader(directory)
        for row in reader:
            for item in row:
                rowtext = rowtext + " " + item
            print(rowtext)
    finally:
        directory.close()
    menu()

menu()
