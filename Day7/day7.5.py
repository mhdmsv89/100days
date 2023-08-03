import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = len(stages)-1

word_list = ["ardvark", "baboon","camel"]
chosen_word = random.choice(word_list)
print(f"the chosen word is {chosen_word}")
display = []

for letter in chosen_word:
    display += "_"
print(f"{''.join(display)}")

end_of_game = False

while not end_of_game:
    guess_letter = input("Guess a letter").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if guess_letter not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You Lose")
        if letter == guess_letter:
            display[position] = letter
            print(f"{''.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You Win")