year = int(input("What year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its a leap year")
        else:
            print("It is NOT a leap year")
    else :
        print("It is a leap year")
else:
    print("It is NOT a leap year")