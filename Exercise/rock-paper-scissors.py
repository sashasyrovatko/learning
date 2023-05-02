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
import random
choice_list = [rock, paper, scissors]
# list_items = len(choice_list)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("You taped an invalid number, you lose")
else:
 print(choice_list[choice])
# your_choice = random.choice(choice)
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(choice_list[computer_choice])
# print(your_choice)

if choice == 0 and computer_choice == 2:
    print("YOU win")
elif computer_choice == 0 and choice == 2:
    print("You lose")
elif computer_choice > choice:
    print("You lose")
elif choice > computer_choice:
    print("You win")
elif computer_choice == choice:
    print("it's draw")
elif choice >= 3 or choice < 0:
    print("You taped an invalid number, you lose")