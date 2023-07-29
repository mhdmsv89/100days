print("Welcome to treasure island, your mission is to find the treasure")
a = input("You are standing on the beach and you see two roads one to the left and the other to the right, \n"
          "the left road goes to the jungle and the right road goes along the beach, \n"
          "which side do you go left or right ?")
lower_a = a.lower()
if lower_a == "left":
    b = input(print("you are now deep in the jungle and you see a lake \n"
                    "do you swim into the lake or wait "))
    lower_b = b.lower()
    if lower_b == "wait":
        c = input(print("while you waiting you notice a cave and go inside \n"
                        "inside the cave you see three doors, red , blue and yellow\n"
                        "which door you choose "))
        lower_c = c.lower()
        if lower_c == "yellow":
            print("Congratulation, you found the treasure inside, you WIN! ")
        else :
            print("You have been Killed by snakes, GAME OVER")
    else:
        print("You have been Killed by sharks, GAME OVER!")
else:
    print("Game Over")