# import random
#
# if random.randint(0, 1) == 0:
#     print("Heads")
# else:
#     print("Tails")
#
# names_string = input("Give me everybody's names,separated by comma.")
# names = names_string.split(",")
# print(f"{random.choice(names)} is going to buy")
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_rock = [rock, paper, scissors]
# comp_choice = random.choice(list_rock)
# you_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#
# if you_choice >= 3 or you_choice < 0:
#     print("You taped an invalid number, you lose")
# else:
#     print(list_rock[you_choice])
# print(list_rock[you_choice])
# print(comp_choice)
#
#
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# total_height = 0
# for n in student_heights:
#     total_height = total_height + n
# print(total_height)
# numbers = 0
# for n in student_heights:
#     numbers += 1
# print(numbers)
# total = 0
# for number in range(0, 101, 2):
#     total += number
# print(total)
# for numbers in range(1, 101):
#     if numbers % 3 == 0 and numbers % 5 == 0:
#         print("fizzbuzz")
#     elif numbers % 3 == 0:
#         print("fizz")
#     elif numbers % 5 == 0:
#         print("buzz")
#     else:
#         print(numbers)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# password = ""
# for b in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for b in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for b in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)
password_list = []
for b in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for b in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for b in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for b in password_list:
    password += b
print(password)