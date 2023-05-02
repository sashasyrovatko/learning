import random
from img import word_list, stages
lives = 6

chosen_word = random.choice(word_list)
print(stages[6])
display = []
chw = len(chosen_word)
for _ in range(chw):
    display += "_"
print(display)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(chw):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You Lose")
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
    print(display)



