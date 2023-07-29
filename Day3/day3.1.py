print("Welcome to the roller coaster")
h = int(input("Please insert your height in centimeter"))
bill = 0
if h >= 120:
    print("You can ride the roller coaster")
    age = int(input("Please insert your age"))
    if age < 12:
        bill = 5
        print("Your ticket cost 5$")
    elif age < 18:
        bill = 7
        print("Your ticket cost 7$")
    elif 45 <= age <= 55:
        bill = 0
        print("your ticket is free")
    else:
        bill = 12
        print("Your ticket cost 12$")
    photo = input("Do you want a photo taken ? y or n")
    if photo == "y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry... you have to grow taller before you can ride")
