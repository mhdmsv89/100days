yourAge = input("What is your current age?")
a= int(yourAge)
remaining = 90-a
weeks = remaining*52
days = remaining*365
months = remaining*12

print(f"You have {remaining} years , {months} months , {weeks}  weeks , {days} days")