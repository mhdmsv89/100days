w = input("What is your weight in kilogram?")
h = input("What is your height in Meter")

w_float = float(w)
h_float = float(h)

bmi = w_float / (h_float**2)
result = str(bmi)

print("Your BMI is " + result )