from hangman_words import word_list
from hangman_arts import stages, logo
import random

print(logo)

chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}")

word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []

for _ in range(word_length):
    display += "_"
print(f"{''.join(display)}")

while not end_of_game:
    guess_letter = input("Guess a letter").lower()

    if guess_letter in display:
        print(f"You've already guessed {guess_letter}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter

    if guess_letter not in chosen_word:
        print(f"You've guessed {guess_letter}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])