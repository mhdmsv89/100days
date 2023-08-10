
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the Second number: "))
for o in operation:
    print(o)
operation_symbol = input("Pick an Operation from the line above")
calculation_function = operation[operation_symbol]
answer = calculation_function(num_1,num_2)
print(f"{num_1} {operation_symbol} {num_2} = {answer}")
