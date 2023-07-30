names_string = input("give me everybody's names, separated by a comma.")
names = names_string.split (", ")
names_list = len(names)
import random
random_int = random.randint(0,names_list-1)
random_name = names[random_int]
print(f"{random_name} must pay the bill")