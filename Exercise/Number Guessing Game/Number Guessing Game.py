from random import randint
from art import logo
easy_level = 10
hard_level = 5

number = randint(1, 100)
guess = None


def choice():
    if input("Choose a difficulty.Type 'easy' or 'hard': ") == 'easy':
        return easy_level
    else:
        return hard_level


print_choice = choice()


def game():
    print(logo)
    print("Welcome to the number guessing game.\n"
          "I am thinking of a number between 1 and 100")
    global number
    print(number)
    guess = int(input("Make a guess:"))
    if guess >= number:
        print(f"Too high.\n Guess again.\n ")
        return print_choice - 1
    elif guess < number:
        print(f"Too low.\n Guess again.\n ")
        return print_choice - 1
    else:
        print(f"You got it! The answer was {number}.")

while guess != number:
    print_choice = game()
    print(f"You have {print_choice} attempts remaining to guess the number.")
    if print_choice == 0:
        print("You've run out of guesses, you lose.")
    elif guess != number:
        print("Guess again")
    game()

