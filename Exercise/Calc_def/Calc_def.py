from art import logo
print(logo)
# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2
# multiply
def multiply(n1, n2):
    return n1 * n2
# divide
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide
}
# function = operations["*"]
# function(2, 3)
def calculator():
    num1 = float(input("What's the first number?:"))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation:  ")
        num2 = float(input("What's the next number?:"))
        calculation_functon = operations[operation_symbol]
        answer = calculation_functon(num1, num2)
        print(f"{num1}{operation_symbol}{num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation.:") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()
# operation_symbol = input("Pick an operation: ")
# num3 = int(input("What's the next number?: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")