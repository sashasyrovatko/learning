# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#              print("This is a Even number")
# else:
#     print("This is an odd number")
#
# print("Hello,this is a BMI")
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg "))
# bmi = round(weight / height ** 2)
# if bmi <= 18.5:
#     print(f"Your bmi is {bmi}, you are Underweight")
# elif bmi <= 25:
#     print(f"Your bmi is {bmi},you Have a normal weight")
# elif bmi <= 30:
#     print("Overweight")
# elif bmi <= 35:
#     print("Obese")
# else:
#     print(f"Your bmi is {bmi}< you are CLINICALLY obese")
#
# print(bmi)

year = int(input("Which year do you want to check?"))
# if year % 400 == 0:
#     print("Not leap")
# else:
#     if year % 100 % 400 == 0:
# print("Leap")
#     # elif year % 400 == 0:
#     #     print("Leap")
#     if year % 400 == 1
#     elif:year % 100 == 1:
#     print("Not Leap")
# # else:
# #     print(Nt leap)
# #     if year % 100:
# #         print("Not Leap")
# #         if year % 400:

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
      print("Leap year")
else:
    print("Not Leap year")