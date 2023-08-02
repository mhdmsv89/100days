import random
word_list = ["ardvark", "baboon","camel"]
chosen_word = random.choice(word_list)
print(f"the chosen word is {chosen_word}")
guess_letter = input("Guess a letter").lower()


display = []
for letter in chosen_word:
    display += "_"

print(display)
