print("Welcome to Love Calculator")
name1 = input("What is your name \n")
name2 = input("What is their name ? \n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
both_name = lower_name1+lower_name2
t = both_name.count("t")
r = both_name.count("r")
u = both_name.count("u")
e = both_name.count("e")
true = t+r+u+e
l = both_name.count("l")
o = both_name.count("o")
v = both_name.count("v")
e = both_name.count("e")
love = l+o+v+e
score = int(f"{true}{love}")
if score < 10 or score > 90:
    print(f"Your score is {score} , you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score} , you are alright together")
else:
    print(f"your score is {score}")