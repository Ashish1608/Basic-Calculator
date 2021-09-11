from art import logo
import os


def clear(): return os.system('cls')


def calculate(num1, num2, sign):

    if sign == '+':
        print(f"{num1} {sign} {num2} = {num1+num2}")
        return num1+num2

    elif sign == '-':
        print(f"{num1} {sign} {num2} = {num1-num2}")
        return num1-num2

    elif sign == '*':
        print(f"{num1} {sign} {num2} = {num1*num2}")
        return num1*num2

    elif sign == '/':
        print(f"{num1} {sign} {num2} = {num1/num2}")
        return num1/num2


def should_continue(result):

    carry_on = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if carry_on == 'y':
        first_number = result
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        new_result = calculate(first_number, second_number, operation)
        should_continue(new_result)


repeat = True

while repeat:
    clear()
    print(logo)

    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/\n")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))

    result = calculate(first_number, second_number, operation)

    should_continue(result)
