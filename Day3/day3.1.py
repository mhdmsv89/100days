print("Welcome to the roller coaster")
h = int(input("Please insert your height in centimeter"))
if h >= 120:
    print("You can ride the roller coaster")
    age = int(input("Please insert your age"))
    if age < 12:
        print("Your ticket cost 5$")
    elif 12 <= age <= 18:
        print("Your ticket cost 7$")
    else:
        print("Your ticket cost 12$")
else:
    print("Sorry... you have to grow taller before you can ride")
