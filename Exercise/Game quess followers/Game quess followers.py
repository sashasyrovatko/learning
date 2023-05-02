import random
from game_data import data
from art import logo, vs

# account_name = account_a["name"]
# account_descr = account_a["description"]
# account_country = account_a["country"]
# print(f"{account_name}, a {account_descr}, from{account_country}")

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    #print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"
def check_answer(guess, a_followers, b_followers):
    # if a_followers > b_followers and guess == "a"
    if a_followers > b_followers:
        # if guess == "a":
        #     return True
        # else:
        #     return False
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# def random_choice():
while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
      account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right!Current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry,that's wrong.Final score: {score}")

