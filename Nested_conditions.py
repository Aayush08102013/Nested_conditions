# nested conditional statements:
# medical cause
med_cause = input("Do you have a medical cause: Y or N: ")
# attendence:
att = int(input("Enter your average attendence to class: "))
# if statement:
if med_cause == "Y":
    print("your allowed")
else:
    if att> 75:
        print("your allowed")
    else:
        print("your NOT allowed")

# electrcity project:
units = int(input("enter your units consumed: "))
# statments:
if (units < 50):
    amount = units * 2.60
    tax = 25
elif (units <= 100):
    amount = units * 3.50
    tax = 35
elif (units <= 200):
    amount = units * 5.26
    tax = 45
else:
    amount = units * 8.45
    tax = 75
#total bill:
total = amount + tax
print("the total electicity bill is:", total)

# choice of your ride:
print("select your ride")
print("1. Bike")
print("2. Car")
choice = int(input("enter your choice of ride; 1 or 2:"))
# choice 1:
if choice == 1:
    print("speciefy your bike:")
    print("1. scooter")
    print("2. sports bike")
    choice2 = int(input("enter your speciefiecd bike; 1 or 2:"))
    if choice2 == 1:
        print("you selected a scooter")
    else:
        print("you selected sports bike")
# choice 2:
elif choice == 2:
    print("speciefy your car:")
    print("1. SUV")
    print("2. hatchback")
    choice3 = int(input("enter your speciefiecd car; 1 or 2:"))
    if choice3 == 1:
        print("you selected a SUV")
    else:
        print("you selected hatchback")
else:
    print("invalid input!")