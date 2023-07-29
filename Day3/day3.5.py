print("Welcome to Python pizza delivery")
size = input("What size pizza do you want ? S,M,L")
add_pepperoni = input("Do you want pepperoni ? y or n")
extra_cheese = input("Do you want extra cheese ? y or n")
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "y":
        bill += 2
        if extra_cheese == "y":
            bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "y":
        bill += 3
        if extra_cheese == "y":
            bill += 1
elif size == "L":
    bill = 25
    if add_pepperoni == "y":
        bill +=3
        if extra_cheese == "y":
            bill += 1
print(f"your total bill is {bill}")