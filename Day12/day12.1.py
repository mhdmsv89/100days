import random

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return 10
  else:
    return 5

def game():
  print("Welcome to the Number Guessing Game!")
  print("Guess a number between 1 and 100.")
  answer = random.randint(1, 100)

  turns = difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()



# import random
#
# easy_difficulty = 10
# hard_difficulty = 5
#
# def check_answer(guess, answer, turns):
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")
#
# def difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return easy_difficulty
#   else:
#     return hard_difficulty
#
# def game():
#   print("Welcome to the Number Guessing Game!")
#   print("Guess a number between 1 and 100.")
#   answer = random.randint(1, 100)
#
#   turns = difficulty()
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")
#
#     guess = int(input("Make a guess: "))
#
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")
#
# game()