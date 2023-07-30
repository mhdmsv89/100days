player_choice = int(input("Welcome to rock, paper, scissors game\n"
      "type 0 for rock, 1 for paper and 2 for scissor"))
import random
computer_choice = random.randint(0,2)
choices = ["Rock", "Paper", "Scissors"]


if player_choice == 0 and computer_choice == 0:
    print("its a Draw")
elif player_choice == 0 and computer_choice == 1:
    print("You Lose")
elif player_choice == 0 and computer_choice == 2:
    print("You Win")
elif player_choice == 1 and computer_choice == 0:
    print("You Win")
elif player_choice == 1 and computer_choice == 1:
    print("its a Draw")
elif player_choice == 1 and computer_choice == 2:
    print("You Lose")
elif player_choice == 2 and computer_choice == 0:
    print("You Win")
elif player_choice == 2 and computer_choice == 1:
    print("You Lose")
elif player_choice == 2 and computer_choice == 2:
    print("its a Draw")