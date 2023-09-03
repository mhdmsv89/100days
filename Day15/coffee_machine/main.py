from data import resources
from data import menu
from data import profit
is_on = True


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your {change}$ in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, That's not enough money, Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, enjoy")


while is_on:
    choice = input("What would you like to order? (Espresso/Latte/Cappuccino)").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Remaining water is {resources['water']} ml")
        print(f"Remaining milk is {resources['milk']} ml")
        print(f"Remaining coffee is {resources['coffee']} gr")
        print(f"Remaining money is {profit} $")
    elif choice != "espresso" and choice != "latte" and choice != "cappuccino":
        print(f"{choice} is an invalid input, try again!")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


