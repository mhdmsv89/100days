from game_data import data
import random
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

account_b = random.choice(data)
score = 0
game_continue = True
while game_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)



    print(f"compare a : {format_data(account_a)}.")
    print(f"against b : {format_data(account_b)}.")
    guess = input("Who has more follower ? Type 'A' or 'B' :").lower()


    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're Right, your current score is {score}.")
    else:
        print(f"Sorry, that's Wrong, your final score is {score}.")
        game_continue = False
