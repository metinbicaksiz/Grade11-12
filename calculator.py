from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print("Welcome to the calculator!")
    print(logo)
    should_continue = True

    while should_continue:
        num1 = int(input("Enter first number: "))
        operation = input("Pick an operation:\n + \n -\n * \n /\n ")
        num2 = int(input("Enter second number: "))

        for operation in operations:
            if operation == op:
                result = operations[operation](num1, num2)

                print(result)



calculator()