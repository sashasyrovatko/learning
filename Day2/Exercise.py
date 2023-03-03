# two_digit_number = input("Type a two digit number: ")
# # print(type(two_digit_number))
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# result = int(first_digit) + int(second_digit)
# print(result)

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg :")
# a = float(height)
# b = int(weight)
# result = (b / (a * a))
# print(result)
# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)
#
# age = input("What is your current age?")
# age_as_int = int(age)
#
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# month_remaining = years_remaining * 12
# message = f"You have {days_remaining} days,{weeks_remaining} weeks, and {month_remaining} months left."
# print(message)


print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n")
tip = input("How much tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")
bill_as_int = float(bill)
tip_as_int = int(tip) / 100
people_as_int = int(people)
many = (round((bill_as_int * tip_as_int) + bill_as_int) / people_as_int )
print(many)



bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount} dollars" )