print("Welcome to BMI calculater")
w = float(input("Please insert your weight in kg"))
h = float(input("Please insert your height in m"))
bmi = round( w / (h**2),1)

if bmi < 18.5:
    print(f"Your BMI number is {bmi}, You are underweight")
elif bmi < 25:
    print(f"Your BMI number is {bmi}, You are normal weight")
elif bmi < 30:
    print(f"Your BMI number is {bmi}, You are overweight")
elif bmi < 35:
    print(f"Your BMI number is {bmi}, You are obese")
else:
    print(f"Your BMI number is {bmi}, You are clinically obese")