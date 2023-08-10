
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
def calculator():
    num_1 = float(input("Enter the first number: "))
    for symbol in operation:
        print(symbol)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an Operation from the above")
        num_2 = float(input("Enter the next number: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num_1,num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation.: ") =="y":
            num_1 = answer
        else:
            should_continue = False
            calculator()

calculator()