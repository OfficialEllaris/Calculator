from art import logo
from replit import clear

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculate(first_number, operator, second_number):
    operations = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division,
    }

    if operator in operations:
        return operations[operator](first_number, second_number)
    else:
        return "Invalid operator"

def calculator():
    print(logo)
    first_number = float(input("Enter the first number: "))

    continue_calculation = True

    while continue_calculation:
        operator = input("Choose an operator (+, -, *, /): ")
        second_number = float(input("Enter the next number: "))

        result = calculate(first_number, operator, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        if input(f"Type 'y' to use {result} or 'n' for a new calculation: ") == "y":
            first_number = result
        else:
            clear()
            continue_calculation = False
            calculator()

calculator()