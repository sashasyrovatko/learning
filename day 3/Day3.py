print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("Lets go")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay 5 $")
    elif age <= 18:
        bill = 7
        print("Please,pay 7 $")
    elif age >= 45 and age <= 55:
        print("Have a free rider")
    else:
        print("Please,pay 12 $")
        bill = 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is {bill}")
else:
    print("Sorry.You cant ride")