import random
word_list = ["ardvark", "baboon","camel"]
chosen_word = random.choice(word_list)
print(f"the chosen word is {chosen_word}")

display = []

for letter in chosen_word:
    display += "_"
print(display)

guess_letter = input("Guess a letter").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess_letter:
        display[position] = letter

print(display)