from random import randint
from art import logo
import time

EASY = 10
HARD = 5
number_of_attempts = None

while True:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print(" Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
    print(logo)
    number = randint(1, 100)
    selected_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if selected_difficulty.lower() == 'easy':
        number_of_attempts = EASY
    elif selected_difficulty.lower() == 'hard':
        number_of_attempts = HARD
    elif selected_difficulty.lower() != 'easy' and selected_difficulty.lower() != 'hard':
        print('You are too dumb to play')
        break

    while number_of_attempts > 0:
        print(f"You have a {number_of_attempts} tries")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
            number_of_attempts -= 1
        elif guess < number:
            print("Too low")
            number_of_attempts -= 1
        elif guess == number:
            print("You win")
            time.sleep(5)
            break

    if number_of_attempts == 0:
        print("You lose")
        print(f"Pssst, the correct answer is {number}")
        time.sleep(5)
